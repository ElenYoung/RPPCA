"""
Core RP-PCA algorithm implementation.

This module provides the pure-function implementations of the RP-PCA and
standard PCA decomposition for asset-pricing factor models.

Algorithm Reference
-------------------
Lettau & Pelger (2020), "Estimating latent asset-pricing factors",
Journal of Econometrics.

The key matrix for RP-PCA is:

    S = (1/T) X^T X  +  γ * X_bar * X_bar^T

which is equivalent to performing PCA on:

    (1/(NT)) X^T (I_T + (γ/T) 1 1^T) X

where X is a T×N excess-return matrix, X_bar is the N×1 column vector of
time-series means, and γ is the risk-premium weight.

Special cases:
    γ = -1  →  PCA on the sample covariance matrix  (standard PCA)
    γ =  0  →  PCA on the sample second-moment matrix  (1/T) X^T X
    γ > 0   →  overweight the mean, strengthening weak-factor signals
"""

from __future__ import annotations

import warnings

import numpy as np
from numpy.typing import NDArray


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def rppca_decompose(
    X: NDArray[np.floating],
    n_factors: int,
    gamma: float = 10.0,
    normalize: bool = False,
) -> tuple[NDArray, NDArray, NDArray]:
    """Estimate latent factors and loadings via RP-PCA.

    Parameters
    ----------
    X : ndarray of shape (T, N)
        Excess-return panel.  Each row is one time period, each column is one
        asset.  **Must already be excess returns** (risk-free rate subtracted).
    n_factors : int
        Number of latent factors *K* to extract.
    gamma : float, default 10.0
        Risk-premium weight.  ``gamma = -1`` reduces to standard PCA on the
        covariance matrix.  The paper recommends ``gamma = 10`` for empirical
        applications.
    normalize : bool, default False
        If *True*, each asset is divided by its sample standard deviation
        before the eigendecomposition (correlation-matrix version), and the
        loadings are rescaled back afterwards.  This is more robust when
        assets have very different volatilities.

    Returns
    -------
    loadings : ndarray of shape (N, K)
        Estimated factor loadings  Λ_hat.
    factors : ndarray of shape (T, K)
        Estimated factors  F_hat = X @ Λ_hat @ inv(Λ_hat^T Λ_hat).
    eigenvalues : ndarray of shape (K,)
        The *K* largest eigenvalues of the RP-PCA matrix (before any
        rescaling), useful for diagnostics.

    Notes
    -----
    * **In-sample only.**  The loadings and factors are estimated from the
      full sample ``X``.  For out-of-sample usage, first call
      :func:`rppca_decompose` on the training window, then project new
      returns with :func:`project_factors`.
    * Setting ``gamma = -1`` exactly recovers standard PCA of the sample
      covariance matrix; setting ``gamma = 0`` gives PCA of the second-moment
      matrix ``(1/T) X^T X``.

    Warnings
    --------
    **Do NOT demean the data** before calling this function.  RP-PCA's
    advantage over PCA comes entirely from the mean vector x̄ in the term
    ``γ · x̄ x̄ᵀ``.  If you subtract the column means (``X - X.mean(axis=0)``),
    x̄ becomes zero and the γ parameter has **no effect** — RP-PCA degenerates
    to standard PCA regardless of γ.  Pass raw (un-demeaned) excess returns.
    """
    X = np.asarray(X, dtype=np.float64)
    _check_inputs(X, n_factors)
    T, N = X.shape

    # Optional cross-sectional standardisation
    if normalize:
        std = X.std(axis=0, ddof=0)
        std[std == 0] = 1.0          # guard against zero-variance columns
        X_work = X / std[np.newaxis, :]
    else:
        std = None
        X_work = X

    # --- Build the RP-PCA matrix  S = (1/T) X^T X + γ * x_bar * x_bar^T ---
    # Both terms are N×N.  We never need to form the T×T weight matrix.
    second_moment = X_work.T @ X_work / T          # (N, N)
    x_bar = X_work.mean(axis=0, keepdims=True).T    # (N, 1)

    # Warn if the data appears demeaned — this makes γ irrelevant.
    # Skip for γ=-1 (standard PCA) and γ=0 (second-moment PCA) since the
    # mean term is either cancelled out or absent by design.
    if gamma not in (-1.0, 0.0):
        _warn_if_demeaned(x_bar, second_moment, gamma)

    S = second_moment + gamma * (x_bar @ x_bar.T)   # (N, N)

    # --- Eigen-decomposition (descending order) ---
    eigenvalues, eigenvectors = _top_k_eigh(S, n_factors)

    # Loadings: paper defines Λ_hat = sqrt(N) × eigenvectors
    loadings = eigenvectors * np.sqrt(N)             # (N, K)

    # Undo standardisation
    if normalize:
        loadings = loadings / std[:, np.newaxis]

    # Factors: F_hat = X @ Λ_hat @ inv(Λ_hat^T Λ_hat)
    factors = _compute_factors(X, loadings)          # (T, K)

    return loadings, factors, eigenvalues


def pca_decompose(
    X: NDArray[np.floating],
    n_factors: int,
    normalize: bool = False,
) -> tuple[NDArray, NDArray, NDArray]:
    """Standard PCA on the sample covariance matrix (γ = -1 special case).

    This is a convenience wrapper around :func:`rppca_decompose` with
    ``gamma = -1``.  See that function for the full docstring.
    """
    return rppca_decompose(X, n_factors, gamma=-1.0, normalize=normalize)


def project_factors(
    X_new: NDArray[np.floating],
    loadings: NDArray[np.floating],
) -> NDArray[np.floating]:
    """Project new returns onto previously estimated loadings.

    Parameters
    ----------
    X_new : ndarray of shape (T_new, N)
        New (out-of-sample) excess returns.
    loadings : ndarray of shape (N, K)
        Loadings estimated from a training window.

    Returns
    -------
    factors : ndarray of shape (T_new, K)
        Out-of-sample factor estimates.

    Notes
    -----
    This function is the key building block for **look-ahead-bias-free**
    factor estimation:  estimate loadings on ``X_train``, then call
    ``project_factors(X_test, loadings)`` on subsequent data.
    """
    X_new = np.asarray(X_new, dtype=np.float64)
    loadings = np.asarray(loadings, dtype=np.float64)
    return _compute_factors(X_new, loadings)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _compute_factors(
    X: NDArray[np.floating],
    loadings: NDArray[np.floating],
) -> NDArray[np.floating]:
    """F_hat = X @ Λ @ inv(Λ^T Λ)."""
    LtL = loadings.T @ loadings                     # (K, K)
    return X @ loadings @ np.linalg.inv(LtL)        # (T, K)


def _top_k_eigh(
    S: NDArray[np.floating],
    k: int,
) -> tuple[NDArray, NDArray]:
    """Return the *k* largest eigenvalues / eigenvectors of a symmetric matrix.

    Uses ``numpy.linalg.eigh`` (which returns eigenvalues in *ascending*
    order) and reverses.
    """
    eigenvalues, eigenvectors = np.linalg.eigh(S)
    # Reverse to descending order and take top k
    idx = np.argsort(eigenvalues)[::-1][:k]
    return eigenvalues[idx], eigenvectors[:, idx]


def _warn_if_demeaned(
    x_bar: NDArray[np.floating],
    second_moment: NDArray[np.floating],
    gamma: float,
) -> None:
    """Emit a warning if the data appears to have been time-series demeaned.

    When x_bar ≈ 0, the risk-premium term γ·x̄x̄ᵀ vanishes and RP-PCA
    degenerates to standard PCA on the second-moment matrix regardless of γ.
    This is the most common cause of γ having no effect.
    """
    # Measure the relative magnitude of the mean term vs the second moment
    mean_norm_sq = float((x_bar.T @ x_bar).item())     # ||x_bar||²
    diag_mean = float(np.mean(np.diag(second_moment)))  # avg variance scale

    # The γ-perturbation is γ * x̄x̄ᵀ.  Its spectral norm equals
    # |γ| * ||x̄||², while the typical eigenvalue scale is diag_mean.
    # If the perturbation is < 1e-8 relative to the scale, it's negligible.
    if diag_mean > 0:
        relative_signal = abs(gamma) * mean_norm_sq / diag_mean
    else:
        return  # degenerate data; skip warning

    if relative_signal < 1e-6:
        warnings.warn(
            "The input data appears to be time-series demeaned "
            "(each column has near-zero mean).  "
            "RP-PCA relies on the asset means (x̄) to distinguish itself "
            "from standard PCA: the key matrix is "
            "S = (1/T)XᵀX + γ·x̄x̄ᵀ.  "
            "When x̄ ≈ 0, the γ term vanishes and all γ values produce "
            "identical results.  "
            "Do NOT demean excess returns before calling RP-PCA.  "
            "Pass the raw (un-demeaned) excess returns instead.",
            UserWarning,
            stacklevel=3,
        )


def _check_inputs(X: NDArray, n_factors: int) -> None:
    if X.ndim != 2:
        raise ValueError(f"X must be 2-dimensional, got shape {X.shape}")
    T, N = X.shape
    if n_factors < 1:
        raise ValueError("n_factors must be >= 1")
    if n_factors > min(T, N):
        raise ValueError(
            f"n_factors ({n_factors}) exceeds min(T={T}, N={N})"
        )
