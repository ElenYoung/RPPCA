"""
Utility functions for RP-PCA analysis.

Includes helpers for:
* Selecting the number of factors
* Eigenvalue diagnostics
* Data validation
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def eigenvalue_ratio_test(
    X: NDArray[np.floating],
    max_factors: int = 20,
    gamma: float = 10.0,
) -> tuple[int, NDArray]:
    """Suggest the number of factors using the eigenvalue-ratio test.

    Implements the Ahn & Horenstein (2013) eigenvalue-ratio (ER) criterion
    applied to the RP-PCA matrix.

    The criterion selects  ``k = argmax_{j=1,...,max_factors} λ_j / λ_{j+1}``,
    where λ_j are the eigenvalues of the RP-PCA matrix in descending order.

    Parameters
    ----------
    X : ndarray of shape (T, N)
        Excess-return panel.
    max_factors : int, default 20
        Maximum number of factors to consider.
    gamma : float, default 10.0
        Risk-premium weight for the RP-PCA matrix.

    Returns
    -------
    n_factors : int
        Suggested number of factors.
    ratios : ndarray of shape (max_factors,)
        Eigenvalue ratios  ``λ_j / λ_{j+1}``  for ``j = 1, ..., max_factors``.

    References
    ----------
    Ahn, S.C. & Horenstein, A.R. (2013). "Eigenvalue ratio test for the
    number of factors."  Econometrica 81, 1203–1227.
    """
    X = np.asarray(X, dtype=np.float64)
    T, N = X.shape
    k = min(max_factors + 1, min(T, N))

    # Build the RP-PCA matrix
    second_moment = X.T @ X / T
    x_bar = X.mean(axis=0, keepdims=True).T
    S = second_moment + gamma * (x_bar @ x_bar.T)

    # Full eigendecomposition (descending)
    evals = np.linalg.eigvalsh(S)[::-1]

    # Compute ratios
    n = min(max_factors, len(evals) - 1)
    ratios = evals[:n] / evals[1 : n + 1]

    # Safeguard against division by zero
    ratios = np.where(np.isfinite(ratios), ratios, 0.0)

    n_factors = int(np.argmax(ratios)) + 1
    return n_factors, ratios


def variance_signal(
    X: NDArray[np.floating],
    n_factors: int,
    gamma: float = 10.0,
) -> NDArray[np.floating]:
    """Compute the normalised variance signal for each factor.

    The variance signal is defined as the largest eigenvalues of
    ``Λ Σ_F Λ^T`` divided by the average idiosyncratic variance ``σ_e²``.

    This diagnostic helps identify which factors are strong vs weak.
    A signal ≫ 1 indicates a strong factor; a signal near the bulk
    of eigenvalues indicates a weak factor.

    Parameters
    ----------
    X : ndarray of shape (T, N)
        Excess-return panel.
    n_factors : int
        Number of factors to extract.
    gamma : float, default 10.0
        Risk-premium weight.

    Returns
    -------
    signals : ndarray of shape (n_factors,)
        Normalised variance signal for each factor.
    """
    from rppca.core import rppca_decompose

    X = np.asarray(X, dtype=np.float64)
    T, N = X.shape

    loadings, factors, _ = rppca_decompose(X, n_factors, gamma=gamma)

    # Factor covariance
    Sigma_F = np.cov(factors, rowvar=False, ddof=1)
    Sigma_F = np.atleast_2d(Sigma_F)

    # Systematic covariance eigenvalues
    sys_cov = loadings @ Sigma_F @ loadings.T        # (N, N)
    sys_evals = np.linalg.eigvalsh(sys_cov)[::-1][:n_factors]

    # Average idiosyncratic variance
    residuals = X - factors @ loadings.T
    sigma_e2 = float(np.mean(np.var(residuals, axis=0, ddof=1)))

    if sigma_e2 == 0:
        return sys_evals

    return sys_evals / sigma_e2


def eigenvalue_spectrum(
    X: NDArray[np.floating],
    gamma: float = 10.0,
    n_top: int = 10,
) -> NDArray[np.floating]:
    """Return the top eigenvalues of the RP-PCA matrix.

    Useful for visualising the scree plot and identifying the number of
    factors.

    Parameters
    ----------
    X : ndarray of shape (T, N)
    gamma : float, default 10.0
    n_top : int, default 10

    Returns
    -------
    eigenvalues : ndarray of shape (n_top,)
    """
    X = np.asarray(X, dtype=np.float64)
    T, N = X.shape
    n_top = min(n_top, min(T, N))

    second_moment = X.T @ X / T
    x_bar = X.mean(axis=0, keepdims=True).T
    S = second_moment + gamma * (x_bar @ x_bar.T)

    evals = np.linalg.eigvalsh(S)[::-1]
    return evals[:n_top]
