"""
Unit tests for the RPPCA library.

Tests cover:
1. Core algorithm correctness (PCA special case, RP-PCA matrix construction)
2. Model API (fit / transform / fit_transform)
3. Rolling window (look-ahead bias free)
4. Evaluation metrics
5. Edge cases and input validation
"""

import numpy as np
import pytest
import sys
import os

# Ensure the src directory is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from rppca.core import rppca_decompose, pca_decompose, project_factors
from rppca.model import RPPCA, RollingRPPCA
from rppca.evaluation import (
    max_sharpe_ratio,
    pricing_errors,
    rms_pricing_error,
    idiosyncratic_variance,
    explained_variation_ratio,
)
from rppca.utils import eigenvalue_ratio_test, eigenvalue_spectrum


# ---------------------------------------------------------------------------
# Fixtures: simulated factor model data
# ---------------------------------------------------------------------------

def _simulate_factor_model(
    T: int = 500,
    N: int = 100,
    K: int = 3,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Simulate X = F Λ^T + e  with known factors and loadings."""
    rng = np.random.default_rng(seed)

    # Factors: distinct means and variances
    mu_F = np.array([0.01, 0.005, 0.008])[:K]
    sigma_F = np.array([0.05, 0.03, 0.02])[:K]
    F = rng.normal(size=(T, K)) * sigma_F[np.newaxis, :] + mu_F[np.newaxis, :]

    # Loadings: i.i.d. standard normal / sqrt(N)
    Lambda = rng.normal(size=(N, K)) / np.sqrt(N)

    # Idiosyncratic noise
    sigma_e = 0.02
    e = rng.normal(size=(T, N)) * sigma_e

    X = F @ Lambda.T + e
    return X, F, Lambda, e


@pytest.fixture
def factor_model_data():
    """Standard simulated data for most tests."""
    return _simulate_factor_model(T=500, N=100, K=3, seed=42)


@pytest.fixture
def small_data():
    """Small dataset for quick tests."""
    return _simulate_factor_model(T=60, N=20, K=2, seed=123)


# ---------------------------------------------------------------------------
# 1. Core algorithm tests
# ---------------------------------------------------------------------------

class TestCoreDecomposition:

    def test_output_shapes(self, factor_model_data):
        X, _, _, _ = factor_model_data
        T, N = X.shape
        K = 3
        loadings, factors, eigenvalues = rppca_decompose(X, K, gamma=10.0)

        assert loadings.shape == (N, K)
        assert factors.shape == (T, K)
        assert eigenvalues.shape == (K,)

    def test_eigenvalues_descending(self, factor_model_data):
        X, _, _, _ = factor_model_data
        _, _, eigenvalues = rppca_decompose(X, 5, gamma=10.0)
        assert np.all(np.diff(eigenvalues) <= 1e-10)  # descending

    def test_pca_is_gamma_minus_one(self, factor_model_data):
        """PCA (covariance) should equal RP-PCA with γ=-1."""
        X, _, _, _ = factor_model_data
        K = 3

        loadings_pca, factors_pca, evals_pca = pca_decompose(X, K)
        loadings_rp, factors_rp, evals_rp = rppca_decompose(X, K, gamma=-1.0)

        # Eigenvalues should match
        np.testing.assert_allclose(evals_pca, evals_rp, atol=1e-10)

        # Loadings may differ by sign flips per column
        for k in range(K):
            sign = np.sign(
                loadings_pca[:, k] @ loadings_rp[:, k]
            )
            np.testing.assert_allclose(
                loadings_pca[:, k] * sign, loadings_rp[:, k], atol=1e-10
            )

    def test_gamma_zero_is_second_moment_pca(self, factor_model_data):
        """γ=0 should give PCA on (1/T) X^T X."""
        X, _, _, _ = factor_model_data
        T, N = X.shape
        K = 3

        loadings, _, eigenvalues = rppca_decompose(X, K, gamma=0.0)

        # Manually compute PCA on second moment matrix
        S = X.T @ X / T
        evals_full = np.linalg.eigvalsh(S)[::-1][:K]
        np.testing.assert_allclose(eigenvalues, evals_full, atol=1e-10)

    def test_factors_are_projections(self, factor_model_data):
        """F_hat = X @ Λ_hat @ inv(Λ_hat^T Λ_hat)."""
        X, _, _, _ = factor_model_data
        K = 3
        loadings, factors, _ = rppca_decompose(X, K, gamma=10.0)

        expected = X @ loadings @ np.linalg.inv(loadings.T @ loadings)
        np.testing.assert_allclose(factors, expected, atol=1e-10)

    def test_normalize_option(self, factor_model_data):
        X, _, _, _ = factor_model_data
        K = 3

        # Both should run without error
        l1, f1, e1 = rppca_decompose(X, K, gamma=10.0, normalize=False)
        l2, f2, e2 = rppca_decompose(X, K, gamma=10.0, normalize=True)

        # Shapes should be identical
        assert l1.shape == l2.shape
        assert f1.shape == f2.shape

        # Results should generally differ
        assert not np.allclose(e1, e2)

    def test_larger_gamma_strengthens_signal(self, factor_model_data):
        """Larger γ should increase the eigenvalues of the RP-PCA matrix."""
        X, _, _, _ = factor_model_data
        K = 3

        _, _, evals_0 = rppca_decompose(X, K, gamma=0.0)
        _, _, evals_10 = rppca_decompose(X, K, gamma=10.0)
        _, _, evals_100 = rppca_decompose(X, K, gamma=100.0)

        # The sum of eigenvalues should increase with γ
        assert np.sum(evals_10) >= np.sum(evals_0) - 1e-10
        assert np.sum(evals_100) >= np.sum(evals_10) - 1e-10


class TestProjectFactors:

    def test_project_matches_fit(self, factor_model_data):
        """Projecting training data should match in-sample factors."""
        X, _, _, _ = factor_model_data
        K = 3
        loadings, factors_is, _ = rppca_decompose(X, K, gamma=10.0)
        factors_proj = project_factors(X, loadings)
        np.testing.assert_allclose(factors_is, factors_proj, atol=1e-10)

    def test_oos_shape(self, factor_model_data):
        X, _, _, _ = factor_model_data
        K = 3
        loadings, _, _ = rppca_decompose(X[:400], K, gamma=10.0)
        F_oos = project_factors(X[400:], loadings)
        assert F_oos.shape == (100, K)


# ---------------------------------------------------------------------------
# 2. Model API tests
# ---------------------------------------------------------------------------

class TestRPPCAModel:

    def test_fit_transform(self, factor_model_data):
        X, _, _, _ = factor_model_data
        model = RPPCA(n_factors=3, gamma=10.0)
        factors = model.fit_transform(X)

        assert factors.shape == (X.shape[0], 3)
        assert model.loadings_.shape == (X.shape[1], 3)
        assert model.eigenvalues_.shape == (3,)

    def test_transform_oos(self, factor_model_data):
        X, _, _, _ = factor_model_data
        model = RPPCA(n_factors=3, gamma=10.0)
        model.fit(X[:400])

        F_oos = model.transform(X[400:])
        assert F_oos.shape == (100, 3)

    def test_not_fitted_raises(self):
        model = RPPCA(n_factors=3)
        with pytest.raises(RuntimeError, match="not been fitted"):
            model.transform(np.zeros((10, 5)))

    def test_repr(self):
        model = RPPCA(n_factors=5, gamma=10.0)
        assert "not fitted" in repr(model)
        model.fit(np.random.randn(100, 20))
        assert "fitted" in repr(model)

    def test_evaluation_methods(self, factor_model_data):
        X, _, _, _ = factor_model_data
        model = RPPCA(n_factors=3, gamma=10.0)
        model.fit(X)

        sr = model.get_max_sharpe_ratio()
        assert sr >= 0

        alpha = model.get_pricing_errors(X)
        assert alpha.shape == (X.shape[1],)

        rms = model.get_rms_pricing_error(X)
        assert rms >= 0

        idio = model.get_idiosyncratic_variance(X)
        assert idio >= 0

        evr = model.get_explained_variation(X)
        assert 0 <= evr <= 1


# ---------------------------------------------------------------------------
# 3. Rolling window tests
# ---------------------------------------------------------------------------

class TestRollingRPPCA:

    def test_oos_shape(self, small_data):
        X, _, _, _ = small_data
        T, N = X.shape
        window = 30

        rolling = RollingRPPCA(n_factors=2, gamma=10.0, window=window)
        rolling.fit(X)

        expected_oos_len = T - window
        assert rolling.oos_factors_.shape == (expected_oos_len, 2)
        assert rolling.oos_start_ == window

    def test_no_lookahead_bias(self, small_data):
        """Verify that the rolling estimator only uses past data.

        We do this by checking that modifying future data does NOT change
        the OOS factor estimate at a given time step.
        """
        X, _, _, _ = small_data
        T, N = X.shape
        window = 30
        rng = np.random.default_rng(999)

        # Fit on original data
        rolling1 = RollingRPPCA(n_factors=2, gamma=10.0, window=window)
        rolling1.fit(X)

        # Modify data AFTER the first OOS point (index = window)
        X_modified = X.copy()
        X_modified[window + 5:] += rng.normal(size=(T - window - 5, N)) * 10

        rolling2 = RollingRPPCA(n_factors=2, gamma=10.0, window=window)
        rolling2.fit(X_modified)

        # The first 5 OOS factor estimates should be identical
        # (they only depend on data up to index window+4)
        np.testing.assert_allclose(
            rolling1.oos_factors_[:5],
            rolling2.oos_factors_[:5],
            atol=1e-10,
        )

    def test_min_window_expanding(self, small_data):
        X, _, _, _ = small_data
        T, N = X.shape

        rolling = RollingRPPCA(
            n_factors=2, gamma=10.0, window=30, min_window=10
        )
        rolling.fit(X)

        expected_oos_len = T - 10
        assert rolling.oos_factors_.shape == (expected_oos_len, 2)
        assert rolling.oos_start_ == 10

    def test_oos_evaluation(self, small_data):
        X, _, _, _ = small_data
        window = 30

        rolling = RollingRPPCA(n_factors=2, gamma=10.0, window=window)
        rolling.fit(X)

        sr = rolling.get_oos_max_sharpe_ratio()
        assert np.isfinite(sr)

        rms = rolling.get_oos_rms_pricing_error(X)
        assert rms >= 0

        idio = rolling.get_oos_idiosyncratic_variance(X)
        assert idio >= 0

    def test_not_fitted_raises(self):
        rolling = RollingRPPCA(n_factors=2, window=30)
        with pytest.raises(RuntimeError, match="not been fitted"):
            rolling.get_oos_max_sharpe_ratio()


# ---------------------------------------------------------------------------
# 4. Evaluation metrics tests
# ---------------------------------------------------------------------------

class TestEvaluation:

    def test_max_sharpe_ratio_positive(self, factor_model_data):
        X, F, _, _ = factor_model_data
        sr = max_sharpe_ratio(F)
        assert sr > 0

    def test_max_sharpe_ratio_annualize(self, factor_model_data):
        X, F, _, _ = factor_model_data
        sr_monthly = max_sharpe_ratio(F)
        sr_annual = max_sharpe_ratio(F, annualize=12)
        np.testing.assert_allclose(sr_annual, sr_monthly * np.sqrt(12), atol=1e-10)

    def test_pricing_errors_zero_for_perfect_model(self):
        """If X = F Λ^T exactly, alphas should be zero."""
        rng = np.random.default_rng(42)
        T, N, K = 200, 50, 2
        F = rng.normal(size=(T, K))
        Lambda = rng.normal(size=(N, K))
        X = F @ Lambda.T  # no noise

        alphas = pricing_errors(X, F)
        np.testing.assert_allclose(alphas, 0.0, atol=1e-10)

    def test_rms_pricing_error_nonneg(self, factor_model_data):
        X, _, _, _ = factor_model_data
        _, factors, _ = rppca_decompose(X, 3, gamma=10.0)
        rms = rms_pricing_error(X, factors)
        assert rms >= 0

    def test_idiosyncratic_variance_decreases_with_more_factors(
        self, factor_model_data
    ):
        X, _, _, _ = factor_model_data
        _, f2, _ = rppca_decompose(X, 2, gamma=10.0)
        _, f5, _ = rppca_decompose(X, 5, gamma=10.0)

        idio2 = idiosyncratic_variance(X, f2)
        idio5 = idiosyncratic_variance(X, f5)
        assert idio5 <= idio2 + 1e-10

    def test_explained_variation_ratio_range(self, factor_model_data):
        X, _, _, _ = factor_model_data
        _, factors, _ = rppca_decompose(X, 3, gamma=10.0)
        evr = explained_variation_ratio(X, factors)
        assert 0 <= evr <= 1

    def test_single_factor(self):
        """Ensure metrics work with K=1."""
        rng = np.random.default_rng(7)
        X = rng.normal(size=(200, 30))
        _, factors, _ = rppca_decompose(X, 1, gamma=10.0)

        sr = max_sharpe_ratio(factors)
        assert np.isfinite(sr)

        alphas = pricing_errors(X, factors)
        assert alphas.shape == (30,)


# ---------------------------------------------------------------------------
# 5. Utility tests
# ---------------------------------------------------------------------------

class TestUtils:

    def test_eigenvalue_ratio_test(self, factor_model_data):
        X, _, _, _ = factor_model_data
        n_factors, ratios = eigenvalue_ratio_test(X, max_factors=10, gamma=10.0)
        assert 1 <= n_factors <= 10
        assert ratios.shape[0] <= 10
        assert np.all(ratios >= 0)

    def test_eigenvalue_spectrum(self, factor_model_data):
        X, _, _, _ = factor_model_data
        evals = eigenvalue_spectrum(X, gamma=10.0, n_top=5)
        assert evals.shape == (5,)
        assert np.all(np.diff(evals) <= 1e-10)  # descending


# ---------------------------------------------------------------------------
# 6. Input validation tests
# ---------------------------------------------------------------------------

class TestInputValidation:

    def test_1d_input_raises(self):
        with pytest.raises(ValueError, match="2-dimensional"):
            rppca_decompose(np.zeros(10), 1)

    def test_too_many_factors_raises(self):
        X = np.random.randn(10, 5)
        with pytest.raises(ValueError, match="exceeds"):
            rppca_decompose(X, 6)

    def test_zero_factors_raises(self):
        X = np.random.randn(10, 5)
        with pytest.raises(ValueError, match=">= 1"):
            rppca_decompose(X, 0)


# ---------------------------------------------------------------------------
# 7. Comparison: RP-PCA vs PCA — weak factor detection
# ---------------------------------------------------------------------------

class TestWeakFactorDetection:
    """
    Verify the key theoretical prediction: RP-PCA with γ > 0 should better
    detect weak factors with high Sharpe ratios compared to PCA (γ=-1).
    """

    def test_rppca_higher_sharpe_than_pca(self):
        """Simulate a model with a weak high-SR factor; RP-PCA should win."""
        rng = np.random.default_rng(2024)
        T, N = 500, 200

        # Strong factor (market-like)
        F1 = rng.normal(0.005, 0.05, size=(T, 1))
        Lambda1 = rng.normal(size=(N, 1))

        # Weak factor with HIGH Sharpe ratio
        F2 = rng.normal(0.008, 0.01, size=(T, 1))  # SR ≈ 0.8
        Lambda2 = rng.normal(size=(N, 1)) * 0.1     # very small loadings

        e = rng.normal(0, 0.03, size=(T, N))
        X = F1 @ Lambda1.T + F2 @ Lambda2.T + e

        # Extract 2 factors with both methods
        _, factors_pca, _ = pca_decompose(X, 2)
        _, factors_rp, _ = rppca_decompose(X, 2, gamma=10.0)

        sr_pca = max_sharpe_ratio(factors_pca)
        sr_rp = max_sharpe_ratio(factors_rp)

        # RP-PCA should have a higher (or at least comparable) SR
        # due to better detection of the weak high-SR factor
        assert sr_rp >= sr_pca * 0.9, (
            f"Expected RP-PCA SR ({sr_rp:.4f}) >= 0.9 * PCA SR ({sr_pca:.4f})"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
