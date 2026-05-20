#!/usr/bin/env python
"""
Example: RP-PCA vs PCA on simulated factor model data.

Demonstrates:
1. In-sample estimation with RPPCA and PCA
2. Out-of-sample rolling-window estimation (no look-ahead bias)
3. Comparison of Sharpe ratios, pricing errors, and explained variation
4. Weak factor detection advantage of RP-PCA

Usage:
    python scripts/example_simulation.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import numpy as np
from rppca.model import RPPCA, RollingRPPCA
from rppca.evaluation import max_sharpe_ratio, rms_pricing_error, explained_variation_ratio


def simulate_data(T=600, N=200, seed=2024):
    """Simulate a 4-factor model with one strong and one weak high-SR factor."""
    rng = np.random.default_rng(seed)

    # Factor parameters
    #                  Market   Size    Value   Weak-High-SR
    mu_F = np.array([  0.006,  0.003,  0.004,  0.008])
    sigma_F = np.array([0.045, 0.025,  0.020,  0.010])   # Factor 4: weak variance

    K = len(mu_F)
    F = rng.normal(size=(T, K)) * sigma_F + mu_F

    # Loadings: Market affects all; others are sparser
    Lambda = rng.normal(size=(N, K)) / np.sqrt(N)
    # Make Factor 4 loadings very small (weak factor)
    Lambda[:, 3] *= 0.3

    # Idiosyncratic noise
    e = rng.normal(0, 0.025, size=(T, N))

    X = F @ Lambda.T + e
    return X, F, Lambda, mu_F, sigma_F


def main():
    print("=" * 70)
    print("RP-PCA vs PCA: Simulation Example")
    print("=" * 70)

    # --- Simulate data ---
    T, N = 600, 200
    X, F_true, Lambda_true, mu_F, sigma_F = simulate_data(T, N)
    K = 4

    print(f"\nData: T={T} periods, N={N} assets, K={K} true factors")
    print(f"True factor Sharpe ratios: {mu_F / sigma_F}")
    print(f"True factor variances:     {sigma_F**2}")
    print(f"Factor 4 is WEAK (σ²={sigma_F[3]**2:.4f}) with HIGH SR "
          f"({mu_F[3]/sigma_F[3]:.2f})")

    # =====================================================================
    # 1. IN-SAMPLE COMPARISON
    # =====================================================================
    print("\n" + "=" * 70)
    print("1. IN-SAMPLE COMPARISON")
    print("=" * 70)

    for gamma, label in [(-1.0, "PCA (γ=-1)"), (0.0, "γ=0"), (10.0, "RP-PCA (γ=10)")]:
        model = RPPCA(n_factors=K, gamma=gamma)
        model.fit(X)

        sr = model.get_max_sharpe_ratio()
        rms = model.get_rms_pricing_error(X)
        evr = model.get_explained_variation(X)

        print(f"\n  {label:20s}  |  Max SR: {sr:.4f}  |  "
              f"RMS α: {rms:.6f}  |  Explained Var: {evr:.4f}")

    # =====================================================================
    # 2. OUT-OF-SAMPLE ROLLING WINDOW
    # =====================================================================
    print("\n" + "=" * 70)
    print("2. OUT-OF-SAMPLE (Rolling Window = 240)")
    print("=" * 70)

    window = 240

    for gamma, label in [(-1.0, "PCA (γ=-1)"), (10.0, "RP-PCA (γ=10)")]:
        rolling = RollingRPPCA(n_factors=K, gamma=gamma, window=window)
        rolling.fit(X)

        sr_oos = rolling.get_oos_max_sharpe_ratio()
        rms_oos = rolling.get_oos_rms_pricing_error(X)
        idio_oos = rolling.get_oos_idiosyncratic_variance(X)

        n_oos = X.shape[0] - rolling.oos_start_
        print(f"\n  {label:20s}  |  OOS periods: {n_oos}  |  "
              f"OOS Max SR: {sr_oos:.4f}  |  OOS RMS α: {rms_oos:.6f}  |  "
              f"OOS Idio Var: {idio_oos:.6f}")

    # =====================================================================
    # 3. EFFECT OF γ ON EIGENVALUE SIGNAL
    # =====================================================================
    print("\n" + "=" * 70)
    print("3. EIGENVALUE SIGNAL STRENGTHENING")
    print("=" * 70)

    from rppca.utils import eigenvalue_spectrum

    for gamma in [-1.0, 0.0, 5.0, 10.0, 50.0]:
        evals = eigenvalue_spectrum(X, gamma=gamma, n_top=K + 2)
        evals_str = "  ".join(f"{v:.4f}" for v in evals)
        print(f"  γ={gamma:6.1f}  |  Top eigenvalues: {evals_str}")

    # =====================================================================
    # 4. DEMONSTRATING LOOK-AHEAD BIAS PROTECTION
    # =====================================================================
    print("\n" + "=" * 70)
    print("4. LOOK-AHEAD BIAS CHECK")
    print("=" * 70)

    # In-sample model uses ALL data → look-ahead bias
    model_is = RPPCA(n_factors=K, gamma=10.0)
    model_is.fit(X)
    sr_is = model_is.get_max_sharpe_ratio()

    # Rolling model is strictly causal
    rolling_oos = RollingRPPCA(n_factors=K, gamma=10.0, window=window)
    rolling_oos.fit(X)
    sr_oos = rolling_oos.get_oos_max_sharpe_ratio()

    print(f"\n  In-sample Max SR:      {sr_is:.4f}  (uses future data — biased)")
    print(f"  Out-of-sample Max SR:  {sr_oos:.4f}  (no look-ahead — unbiased)")
    print(f"\n  → For real strategies, always use RollingRPPCA!")

    print("\n" + "=" * 70)
    print("Done.")
    print("=" * 70)


if __name__ == "__main__":
    main()
