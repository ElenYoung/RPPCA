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
