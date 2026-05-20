"""
Evaluation metrics for asset-pricing factor models.

Provides standard measures used to assess how well estimated factors
explain the cross-section of expected returns:

* Maximum Sharpe ratio of the factor-mimicking portfolio
* Pricing errors (alphas) from time-series regressions
* Root-mean-squared pricing error (RMS α)
* Idiosyncratic (unexplained) variance
* Explained variation ratio
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def max_sharpe_ratio(
    factors: NDArray[np.floating],
    annualize: float | None = None,
) -> float:
    """Maximum attainable Sharpe ratio from a linear combination of factors.

    The maximum SR of K factors equals  ``sqrt(μ^T Σ^{-1} μ)``  where μ and
    Σ are the mean vector and covariance matrix of the factors.

    Parameters
    ----------
    factors : ndarray of shape (T, K)
        Estimated factor return series.
    annualize : float or None, default None
        If given, multiply the Sharpe ratio by ``sqrt(annualize)`` (e.g.
        ``annualize=12`` for monthly data → annualised SR).

    Returns
    -------
    sr : float
        Maximum Sharpe ratio (per-period, unless *annualize* is set).
    """
    factors = np.asarray(factors, dtype=np.float64)
    mu = factors.mean(axis=0)                        # (K,)
    cov = np.cov(factors, rowvar=False, ddof=1)      # (K, K)
    # Handle single-factor case where np.cov returns a scalar
    cov = np.atleast_2d(cov)
    sr2 = mu @ np.linalg.solve(cov, mu)
    sr = np.sqrt(max(sr2, 0.0))
    if annualize is not None:
        sr *= np.sqrt(annualize)
    return float(sr)


def pricing_errors(
    X: NDArray[np.floating],
    factors: NDArray[np.floating],
    loadings: NDArray[np.floating] | None = None,
) -> NDArray[np.floating]:
    """Per-asset pricing errors (alphas) from time-series regressions.

    For each asset *i*, run the OLS regression::

        X_{t,i} = α_i + F_t^T β_i + ε_{t,i}

    and return the vector of intercepts α.

    Parameters
    ----------
    X : ndarray of shape (T, N)
        Excess-return panel.
    factors : ndarray of shape (T, K)
        Factor return series (in-sample or out-of-sample).
    loadings : ndarray of shape (N, K) or None
        If provided, the pricing error is computed as
        ``α_i = mean(X_i) - mean(F)^T Λ_i``  (cross-sectional formula).
        If *None*, a full time-series OLS regression is run for each asset.

    Returns
    -------
    alphas : ndarray of shape (N,)
        Pricing errors (intercepts).
    """
    X = np.asarray(X, dtype=np.float64)
    factors = np.asarray(factors, dtype=np.float64)
    T, N = X.shape

    if loadings is not None:
        # Cross-sectional formula: α = E[X] - E[F]^T Λ
        loadings = np.asarray(loadings, dtype=np.float64)
        mu_X = X.mean(axis=0)                       # (N,)
        mu_F = factors.mean(axis=0)                  # (K,)
        alphas = mu_X - loadings @ mu_F              # (N,)
    else:
        # Time-series OLS: X_i = α + F β + ε  for each asset
        # Design matrix: [1, F]
        ones = np.ones((T, 1), dtype=np.float64)
        design = np.hstack([ones, factors])          # (T, K+1)
        # Solve all assets at once: β_hat = (D^T D)^{-1} D^T X
        coef = np.linalg.lstsq(design, X, rcond=None)[0]  # (K+1, N)
        alphas = coef[0, :]                          # intercepts

    return alphas


def rms_pricing_error(
    X: NDArray[np.floating],
    factors: NDArray[np.floating],
    loadings: NDArray[np.floating] | None = None,
) -> float:
    """Root-mean-squared pricing error  ``sqrt( (1/N) Σ α_i² )``.

    Parameters
    ----------
    X, factors, loadings
        See :func:`pricing_errors`.

    Returns
    -------
    rms_alpha : float
    """
    alphas = pricing_errors(X, factors, loadings)
    return float(np.sqrt(np.mean(alphas ** 2)))


def idiosyncratic_variance(
    X: NDArray[np.floating],
    factors: NDArray[np.floating],
    loadings: NDArray[np.floating] | None = None,
) -> float:
    """Average idiosyncratic (unexplained) variance across assets.

    For each asset, the residual variance is ``Var(X_i - F^T β_i)``
    (from the time-series regression).  This function returns the
    cross-sectional average.

    Parameters
    ----------
    X : ndarray of shape (T, N)
    factors : ndarray of shape (T, K)
    loadings : ndarray of shape (N, K) or None
        If *None*, OLS betas are estimated from the data.

    Returns
    -------
    avg_idio_var : float
    """
    X = np.asarray(X, dtype=np.float64)
    factors = np.asarray(factors, dtype=np.float64)
    T, N = X.shape

    if loadings is not None:
        loadings = np.asarray(loadings, dtype=np.float64)
        # Residuals: e = X - F @ Λ^T  (using loadings directly as betas
        # under the normalisation in the paper)
        # But more precisely, run OLS to get betas
        betas = _ols_betas(factors, X)               # (K, N)
        alpha = X.mean(axis=0) - factors.mean(axis=0) @ betas
        fitted = factors @ betas + alpha[np.newaxis, :]
    else:
        ones = np.ones((T, 1), dtype=np.float64)
        design = np.hstack([ones, factors])
        coef = np.linalg.lstsq(design, X, rcond=None)[0]
        fitted = design @ coef

    residuals = X - fitted                           # (T, N)
    var_per_asset = np.var(residuals, axis=0, ddof=1)  # (N,)
    return float(np.mean(var_per_asset))


def explained_variation_ratio(
    X: NDArray[np.floating],
    factors: NDArray[np.floating],
) -> float:
    """Fraction of total variance explained by the factors.

    Computed as  ``1 - (avg idio var) / (avg total var)``.

    Parameters
    ----------
    X : ndarray of shape (T, N)
    factors : ndarray of shape (T, K)

    Returns
    -------
    ratio : float
        Between 0 and 1.
    """
    total_var = float(np.mean(np.var(X, axis=0, ddof=1)))
    idio_var = idiosyncratic_variance(X, factors)
    if total_var == 0:
        return 0.0
    return 1.0 - idio_var / total_var


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ols_betas(
    factors: NDArray[np.floating],
    X: NDArray[np.floating],
) -> NDArray[np.floating]:
    """OLS betas: β = (F^T F)^{-1} F^T X   (without intercept demeaning).

    This uses the *demeaned* version internally so the intercept is absorbed.

    Returns
    -------
    betas : ndarray of shape (K, N)
    """
    F_dm = factors - factors.mean(axis=0, keepdims=True)
    X_dm = X - X.mean(axis=0, keepdims=True)
    FtF = F_dm.T @ F_dm
    FtX = F_dm.T @ X_dm
    return np.linalg.solve(FtF, FtX)                # (K, N)
