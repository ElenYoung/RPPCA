"""
Scikit-learn-style model classes for RP-PCA.

Provides two main classes:

* :class:`RPPCA` — in-sample estimation (fit / transform / fit_transform).
* :class:`RollingRPPCA` — rolling-window out-of-sample estimation that is
  strictly free of look-ahead bias (no future functions).
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from rppca.core import rppca_decompose, project_factors
from rppca.evaluation import (
    max_sharpe_ratio,
    pricing_errors,
    rms_pricing_error,
    idiosyncratic_variance,
    explained_variation_ratio,
)


class RPPCA:
    """Risk-Premium PCA estimator for latent asset-pricing factors.

    This class estimates latent factors and loadings from a panel of excess
    returns using the RP-PCA method of Lettau & Pelger (2020).

    .. warning::
       :meth:`fit` uses the **full sample** to estimate loadings and factors.
       This is an **in-sample** procedure and contains look-ahead bias if
       used naively in a trading strategy.  For out-of-sample / real-time
       usage, see :class:`RollingRPPCA`.

    Parameters
    ----------
    n_factors : int, default 5
        Number of latent factors *K* to extract.
    gamma : float, default 10.0
        Risk-premium weight.

        * ``gamma = -1``: standard PCA on the covariance matrix.
        * ``gamma = 0``: PCA on the second-moment matrix.
        * ``gamma > 0``: overweight the mean → stronger weak-factor detection.

        The paper recommends ``gamma = 10`` for empirical applications.
    normalize : bool, default False
        If *True*, standardise each asset by its sample standard deviation
        before the eigendecomposition (correlation-matrix version).

    Attributes (available after :meth:`fit`)
    -----------------------------------------
    loadings_ : ndarray of shape (N, K)
    factors_ : ndarray of shape (T, K)
    eigenvalues_ : ndarray of shape (K,)
    mean_ : ndarray of shape (N,)
        Per-asset time-series mean of the training data (used internally
        when ``normalize=True``).
    std_ : ndarray of shape (N,) or None
        Per-asset standard deviation (only stored when ``normalize=True``).

    Examples
    --------
    >>> import numpy as np
    >>> from rppca import RPPCA
    >>> X = np.random.randn(600, 100)          # T=600, N=100
    >>> model = RPPCA(n_factors=5, gamma=10)
    >>> model.fit(X)
    >>> print(model.factors_.shape)             # (600, 5)
    >>> print(model.loadings_.shape)            # (100, 5)
    >>> # Out-of-sample projection
    >>> X_new = np.random.randn(12, 100)
    >>> F_oos = model.transform(X_new)
    >>> print(F_oos.shape)                      # (12, 5)
    """

    def __init__(
        self,
        n_factors: int = 5,
        gamma: float = 10.0,
        normalize: bool = False,
    ):
        self.n_factors = n_factors
        self.gamma = gamma
        self.normalize = normalize

        # Will be set by fit()
        self.loadings_: NDArray | None = None
        self.factors_: NDArray | None = None
        self.eigenvalues_: NDArray | None = None
        self.mean_: NDArray | None = None
        self.std_: NDArray | None = None
        self._is_fitted = False

    # ------------------------------------------------------------------
    # Core API
    # ------------------------------------------------------------------

    def fit(self, X: NDArray[np.floating]) -> "RPPCA":
        """Estimate loadings and factors from the full sample (in-sample).

        Parameters
        ----------
        X : ndarray of shape (T, N)
            Excess-return panel.

        Returns
        -------
        self
        """
        X = np.asarray(X, dtype=np.float64)
        self.mean_ = X.mean(axis=0)
        self.std_ = X.std(axis=0, ddof=0) if self.normalize else None

        loadings, factors, eigenvalues = rppca_decompose(
            X,
            n_factors=self.n_factors,
            gamma=self.gamma,
            normalize=self.normalize,
        )
        self.loadings_ = loadings
        self.factors_ = factors
        self.eigenvalues_ = eigenvalues
        self._is_fitted = True
        return self

    def transform(self, X_new: NDArray[np.floating]) -> NDArray[np.floating]:
        """Project new returns onto the estimated loadings (out-of-sample).

        This is the **look-ahead-bias-free** way to obtain factor estimates
        for periods not included in the training sample.

        Parameters
        ----------
        X_new : ndarray of shape (T_new, N)
            New excess returns.

        Returns
        -------
        factors : ndarray of shape (T_new, K)
        """
        self._check_is_fitted()
        return project_factors(X_new, self.loadings_)

    def fit_transform(self, X: NDArray[np.floating]) -> NDArray[np.floating]:
        """Fit the model and return the in-sample factors.

        Parameters
        ----------
        X : ndarray of shape (T, N)

        Returns
        -------
        factors : ndarray of shape (T, K)
        """
        self.fit(X)
        return self.factors_

    # ------------------------------------------------------------------
    # Evaluation helpers
    # ------------------------------------------------------------------

    def get_max_sharpe_ratio(
        self,
        factors: NDArray[np.floating] | None = None,
        annualize: float | None = None,
    ) -> float:
        """Maximum Sharpe ratio of the estimated factors.

        Parameters
        ----------
        factors : ndarray or None
            If *None*, uses the in-sample ``self.factors_``.
        annualize : float or None
            See :func:`rppca.evaluation.max_sharpe_ratio`.
        """
        if factors is None:
            self._check_is_fitted()
            factors = self.factors_
        return max_sharpe_ratio(factors, annualize=annualize)

    def get_pricing_errors(
        self,
        X: NDArray[np.floating],
        factors: NDArray[np.floating] | None = None,
    ) -> NDArray[np.floating]:
        """Per-asset pricing errors (alphas).

        Parameters
        ----------
        X : ndarray of shape (T, N)
        factors : ndarray or None
            If *None*, uses the in-sample ``self.factors_``.
        """
        if factors is None:
            self._check_is_fitted()
            factors = self.factors_
        return pricing_errors(X, factors)

    def get_rms_pricing_error(
        self,
        X: NDArray[np.floating],
        factors: NDArray[np.floating] | None = None,
    ) -> float:
        """Root-mean-squared pricing error."""
        if factors is None:
            self._check_is_fitted()
            factors = self.factors_
        return rms_pricing_error(X, factors)

    def get_idiosyncratic_variance(
        self,
        X: NDArray[np.floating],
        factors: NDArray[np.floating] | None = None,
    ) -> float:
        """Average idiosyncratic variance."""
        if factors is None:
            self._check_is_fitted()
            factors = self.factors_
        return idiosyncratic_variance(X, factors)

    def get_explained_variation(
        self,
        X: NDArray[np.floating],
        factors: NDArray[np.floating] | None = None,
    ) -> float:
        """Fraction of total variance explained."""
        if factors is None:
            self._check_is_fitted()
            factors = self.factors_
        return explained_variation_ratio(X, factors)

    # ------------------------------------------------------------------
    # Private
    # ------------------------------------------------------------------

    def _check_is_fitted(self) -> None:
        if not self._is_fitted:
            raise RuntimeError(
                "Model has not been fitted yet. Call .fit(X) first."
            )

    def __repr__(self) -> str:
        status = "fitted" if self._is_fitted else "not fitted"
        return (
            f"RPPCA(n_factors={self.n_factors}, gamma={self.gamma}, "
            f"normalize={self.normalize}, status={status})"
        )


class RollingRPPCA:
    """Rolling-window RP-PCA estimator — strictly look-ahead-bias free.

    At each time step *t*, the model:

    1. Estimates loadings from the training window ``X[t-window+1 : t+1]``
       (the most recent *window* observations ending at *t*).
    2. Projects the **next** observation ``X[t+1]`` onto those loadings to
       obtain an out-of-sample factor estimate.

    This mirrors the procedure described in Section 7 of Lettau & Pelger
    (2020), which uses a 20-year (240-month) rolling window.

    Parameters
    ----------
    n_factors : int, default 5
    gamma : float, default 10.0
    window : int, default 240
        Length of the rolling estimation window (in number of periods).
    normalize : bool, default False
    min_window : int or None, default None
        If set, allow an expanding window for the first ``window - min_window``
        periods (starting from ``min_window`` observations).  If *None*, the
        first ``window - 1`` periods have no out-of-sample estimate.

    Attributes (available after :meth:`fit`)
    -----------------------------------------
    oos_factors_ : ndarray of shape (T_oos, K)
        Out-of-sample factor estimates aligned with ``X[window:]``.
    oos_start_ : int
        The index in the original *X* array where out-of-sample estimates
        begin (equals *window* if ``min_window`` is *None*).
    loadings_history_ : list[ndarray]
        Sequence of (N, K) loading matrices, one per estimation step.
    sharpe_weights_history_ : list[ndarray]
        Optimal max-Sharpe portfolio weights estimated at each step.

    Examples
    --------
    >>> import numpy as np
    >>> from rppca import RollingRPPCA
    >>> X = np.random.randn(600, 100)
    >>> rolling = RollingRPPCA(n_factors=5, gamma=10, window=240)
    >>> rolling.fit(X)
    >>> print(rolling.oos_factors_.shape)        # (360, 5)
    >>> print(rolling.oos_start_)                # 240
    """

    def __init__(
        self,
        n_factors: int = 5,
        gamma: float = 10.0,
        window: int = 240,
        normalize: bool = False,
        min_window: int | None = None,
    ):
        self.n_factors = n_factors
        self.gamma = gamma
        self.window = window
        self.normalize = normalize
        self.min_window = min_window

        # Will be set by fit()
        self.oos_factors_: NDArray | None = None
        self.oos_start_: int | None = None
        self.loadings_history_: list[NDArray] | None = None
        self.sharpe_weights_history_: list[NDArray] | None = None
        self._is_fitted = False

    def fit(self, X: NDArray[np.floating]) -> "RollingRPPCA":
        """Run the rolling-window estimation.

        Parameters
        ----------
        X : ndarray of shape (T, N)
            Full panel of excess returns.

        Returns
        -------
        self
        """
        X = np.asarray(X, dtype=np.float64)
        T, N = X.shape

        start = self.min_window if self.min_window is not None else self.window
        if start < self.n_factors + 1:
            raise ValueError(
                f"Window (or min_window) must be > n_factors. "
                f"Got {start} <= {self.n_factors}."
            )
        if start > T - 1:
            raise ValueError(
                f"Not enough data: need at least {start + 1} periods, "
                f"got T={T}."
            )

        oos_factors_list: list[NDArray] = []
        loadings_history: list[NDArray] = []
        sharpe_weights_history: list[NDArray] = []

        for t in range(start, T):
            # Training window: [t - w + 1, t] inclusive → Python slice [t-w+1 : t+1]
            w = min(t, self.window)          # expanding if t < self.window
            X_train = X[t - w: t]            # (w, N) — uses data up to t-1

            # Estimate loadings on training window
            loadings, factors_train, _ = rppca_decompose(
                X_train,
                n_factors=self.n_factors,
                gamma=self.gamma,
                normalize=self.normalize,
            )
            loadings_history.append(loadings)

            # Compute in-sample max-Sharpe weights for the training window
            mu_f = factors_train.mean(axis=0)
            cov_f = np.cov(factors_train, rowvar=False, ddof=1)
            cov_f = np.atleast_2d(cov_f)
            try:
                w_sr = np.linalg.solve(cov_f, mu_f)
            except np.linalg.LinAlgError:
                w_sr = np.zeros_like(mu_f)
            sharpe_weights_history.append(w_sr)

            # Out-of-sample: project the NEXT return (at time t)
            X_oos = X[t: t + 1]                      # (1, N)
            F_oos = project_factors(X_oos, loadings)  # (1, K)
            oos_factors_list.append(F_oos[0])

        self.oos_factors_ = np.array(oos_factors_list)    # (T - start, K)
        self.oos_start_ = start
        self.loadings_history_ = loadings_history
        self.sharpe_weights_history_ = sharpe_weights_history
        self._is_fitted = True
        return self

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    def get_oos_max_sharpe_ratio(
        self,
        X: NDArray[np.floating] | None = None,
        annualize: float | None = None,
    ) -> float:
        """Out-of-sample maximum Sharpe ratio.

        Uses the max-Sharpe portfolio weights estimated from each training
        window to compute an out-of-sample portfolio return series, then
        reports its Sharpe ratio.

        Parameters
        ----------
        X : ndarray of shape (T, N) or None
            If *None*, the Sharpe ratio is computed directly from the
            out-of-sample factor estimates.
        annualize : float or None

        Returns
        -------
        sr : float
        """
        self._check_is_fitted()

        if X is None:
            # Simple: SR from the OOS factor return series
            return max_sharpe_ratio(self.oos_factors_, annualize=annualize)

        # Use the rolling max-SR portfolio weights
        X = np.asarray(X, dtype=np.float64)
        T_total = X.shape[0]
        start = self.oos_start_
        n_oos = T_total - start

        oos_returns = np.empty(n_oos)
        for i in range(n_oos):
            t = start + i
            w_sr = self.sharpe_weights_history_[i]
            F_t = self.oos_factors_[i]
            oos_returns[i] = w_sr @ F_t

        mu = oos_returns.mean()
        std = oos_returns.std(ddof=1)
        sr = mu / std if std > 0 else 0.0
        if annualize is not None:
            sr *= np.sqrt(annualize)
        return float(sr)

    def get_oos_pricing_errors(
        self, X: NDArray[np.floating],
    ) -> NDArray[np.floating]:
        """Out-of-sample pricing errors.

        Parameters
        ----------
        X : ndarray of shape (T, N)
            Full return panel (the OOS portion ``X[oos_start_:]`` is used).

        Returns
        -------
        alphas : ndarray of shape (N,)
        """
        self._check_is_fitted()
        X = np.asarray(X, dtype=np.float64)
        X_oos = X[self.oos_start_:]
        return pricing_errors(X_oos, self.oos_factors_)

    def get_oos_rms_pricing_error(self, X: NDArray[np.floating]) -> float:
        """Out-of-sample RMS pricing error."""
        self._check_is_fitted()
        X = np.asarray(X, dtype=np.float64)
        X_oos = X[self.oos_start_:]
        return rms_pricing_error(X_oos, self.oos_factors_)

    def get_oos_idiosyncratic_variance(self, X: NDArray[np.floating]) -> float:
        """Out-of-sample average idiosyncratic variance."""
        self._check_is_fitted()
        X = np.asarray(X, dtype=np.float64)
        X_oos = X[self.oos_start_:]
        return idiosyncratic_variance(X_oos, self.oos_factors_)

    # ------------------------------------------------------------------
    # Private
    # ------------------------------------------------------------------

    def _check_is_fitted(self) -> None:
        if not self._is_fitted:
            raise RuntimeError(
                "Model has not been fitted yet. Call .fit(X) first."
            )

    def __repr__(self) -> str:
        status = "fitted" if self._is_fitted else "not fitted"
        return (
            f"RollingRPPCA(n_factors={self.n_factors}, gamma={self.gamma}, "
            f"window={self.window}, normalize={self.normalize}, "
            f"status={status})"
        )
