# RPPCA — Risk-Premium PCA for Asset Pricing

<p align="center">
  <em>Estimate latent asset-pricing factors that explain both covariance and expected returns.</em>
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#algorithm">Algorithm</a> •
  <a href="#api-reference">API Reference</a> •
  <a href="#look-ahead-bias">Look-Ahead Bias</a> •
  <a href="#citation">Citation</a>
</p>

---

## Overview

**RPPCA** is a Python implementation of the **Risk-Premium PCA (RP-PCA)** method from:

> Lettau, M. & Pelger, M. (2020). *"Estimating latent asset-pricing factors."*
> Journal of Econometrics, 218(1), 1–31.

Standard PCA finds factors that maximize explained **variance**, but ignores **expected returns**. RP-PCA generalizes PCA by adding a penalty term for pricing errors, enabling it to:

- 🔍 **Detect weak factors** with high Sharpe ratios that PCA misses entirely
- 📈 **Produce factors with higher Sharpe ratios** — often 2× those of PCA
- 📉 **Achieve smaller out-of-sample pricing errors**
- 📊 **Explain the same amount of variance** as conventional PCA

## Installation

```bash
pip install rppca
```

**Requirements:** Python ≥ 3.9, NumPy ≥ 1.21

## Quick Start

### In-Sample Estimation

```python
import numpy as np
from rppca import RPPCA

# X: excess returns matrix (T periods × N assets)
X = np.random.randn(600, 200)

# Estimate 5 factors with γ=10 (paper's recommended value)
model = RPPCA(n_factors=5, gamma=10)
model.fit(X)

# Access results
print(model.factors_.shape)       # (600, 5)
print(model.loadings_.shape)      # (200, 5)
print(model.eigenvalues_)         # Top 5 eigenvalues

# Evaluation metrics
print(f"Max Sharpe Ratio: {model.get_max_sharpe_ratio():.4f}")
print(f"RMS Pricing Error: {model.get_rms_pricing_error(X):.6f}")
print(f"Explained Variation: {model.get_explained_variation(X):.2%}")
```

### Out-of-Sample Estimation (No Look-Ahead Bias)

```python
from rppca import RollingRPPCA

# Rolling window: estimate loadings on past 240 months, project forward
rolling = RollingRPPCA(n_factors=5, gamma=10, window=240)
rolling.fit(X)

# Out-of-sample factors (strictly causal — no future information used)
print(rolling.oos_factors_.shape)  # (360, 5) — T minus window
print(rolling.oos_start_)          # 240

# Out-of-sample evaluation
print(f"OOS Max Sharpe Ratio: {rolling.get_oos_max_sharpe_ratio():.4f}")
print(f"OOS RMS α: {rolling.get_oos_rms_pricing_error(X):.6f}")
```

### Compare RP-PCA vs Standard PCA

```python
from rppca import RPPCA

# Standard PCA (γ = -1)
pca = RPPCA(n_factors=5, gamma=-1)
pca.fit(X)

# RP-PCA (γ = 10)
rppca = RPPCA(n_factors=5, gamma=10)
rppca.fit(X)

print(f"PCA    Max SR: {pca.get_max_sharpe_ratio():.4f}")
print(f"RP-PCA Max SR: {rppca.get_max_sharpe_ratio():.4f}")  # typically 2× higher
```

### Functional API

```python
from rppca import rppca_decompose, pca_decompose

# RP-PCA
loadings, factors, eigenvalues = rppca_decompose(X, n_factors=5, gamma=10)

# Standard PCA (convenience wrapper)
loadings, factors, eigenvalues = pca_decompose(X, n_factors=5)
```

## Algorithm

### Factor Model

Excess returns follow an approximate factor model:

```
X = F · Λᵀ + e
```

where **X** is T×N (periods × assets), **F** is T×K (latent factors), **Λ** is N×K (loadings), and **e** is the idiosyncratic residual.

### RP-PCA Matrix

RP-PCA performs eigendecomposition on a modified second-moment matrix:

```
S = (1/T) XᵀX + γ · X̄ X̄ᵀ
```

where X̄ is the N×1 vector of time-series means of each asset.

This is equivalent to PCA on:

```
(1/NT) Xᵀ (I_T + (γ/T) 𝟏𝟏ᵀ) X
```

### Estimation Steps

| Step | Operation | Output |
|------|-----------|--------|
| 1 | Compute `S = (1/T) XᵀX + γ · X̄X̄ᵀ` | N×N matrix |
| 2 | Eigendecompose S, take top K eigenvectors | v₁, ..., v_K |
| 3 | Loadings: `Λ̂ = √N · [v₁ ... v_K]` | N×K matrix |
| 4 | Factors: `F̂ = X · Λ̂ · (Λ̂ᵀΛ̂)⁻¹` | T×K matrix |

### Role of γ (Risk-Premium Weight)

| Value | Effect |
|-------|--------|
| `γ = -1` | Standard PCA on the **covariance** matrix |
| `γ = 0` | PCA on the **second-moment** matrix (1/T)XᵀX |
| `γ > 0` | Overweight the mean → strengthens weak-factor signal |
| `γ = 10` | **Recommended** by the paper for empirical applications |

The key insight: a larger γ increases the eigenvalue signal of factors with high Sharpe ratios, making weak-but-important pricing factors detectable.

### Signal Strengthening

The population limit of S converges to:

```
Λ (Σ_F + (1+γ) μ_F μ_Fᵀ) Λᵀ + Var(e)
```

For PCA (γ=-1), the signal is driven only by **variance** Σ_F. For RP-PCA (γ>0), the **mean** μ_F also contributes, boosting weak factors that have high Sharpe ratios (large μ_F relative to Σ_F).

## Look-Ahead Bias

> ⚠️ **Critical for quantitative strategies**

### The Problem

The in-sample RP-PCA estimation uses **the full sample** to compute:
- The mean vector X̄ = (1/T) Σ X_t — includes future returns
- The second-moment matrix (1/T) XᵀX — includes future returns
- The eigendecomposition — depends on all of the above

**This introduces look-ahead bias (未来函数).** If you estimate factors at time t using data that includes t+1, t+2, ..., your strategy is peeking into the future.

### The Solution

Use `RollingRPPCA` for any application where causality matters:

```python
from rppca import RollingRPPCA

rolling = RollingRPPCA(
    n_factors=5,
    gamma=10,
    window=240,       # 20-year rolling window (as in the paper)
)
rolling.fit(X)        # Internally: at each t, only uses X[t-240:t]
```

**At each time step t**, the rolling estimator:
1. Estimates loadings from `X[t-window : t]` only (historical data)
2. Projects `X[t]` onto those loadings → out-of-sample factor at t
3. Never uses any data from t+1 onwards

### In-Sample vs Out-of-Sample Summary

| | `RPPCA` (in-sample) | `RollingRPPCA` (out-of-sample) |
|---|---|---|
| **Data used** | Full sample [1, T] | Rolling window [t-w, t] |
| **Look-ahead bias** | ⚠️ **Yes** | ✅ **No** |
| **Use case** | Academic research, model evaluation | Live trading, backtesting |
| **Sharpe ratio** | Upward-biased | Unbiased |
| **Paper reference** | Sections 2–6 | Section 7 |

## API Reference

### Classes

#### `RPPCA(n_factors=5, gamma=10.0, normalize=False)`

In-sample RP-PCA estimator.

| Method | Description |
|--------|-------------|
| `.fit(X)` | Estimate loadings & factors from full sample |
| `.transform(X_new)` | Project new data onto estimated loadings |
| `.fit_transform(X)` | Fit and return in-sample factors |
| `.get_max_sharpe_ratio()` | Maximum Sharpe ratio of the factors |
| `.get_pricing_errors(X)` | Per-asset pricing errors (alphas) |
| `.get_rms_pricing_error(X)` | Root-mean-squared pricing error |
| `.get_idiosyncratic_variance(X)` | Average unexplained variance |
| `.get_explained_variation(X)` | Fraction of variance explained |

#### `RollingRPPCA(n_factors=5, gamma=10.0, window=240, normalize=False, min_window=None)`

Rolling-window estimator — strictly look-ahead-bias free.

| Method | Description |
|--------|-------------|
| `.fit(X)` | Run rolling-window estimation |
| `.get_oos_max_sharpe_ratio()` | Out-of-sample max Sharpe ratio |
| `.get_oos_pricing_errors(X)` | Out-of-sample pricing errors |
| `.get_oos_rms_pricing_error(X)` | Out-of-sample RMS α |
| `.get_oos_idiosyncratic_variance(X)` | Out-of-sample idiosyncratic variance |

| Attribute | Description |
|-----------|-------------|
| `.oos_factors_` | (T_oos, K) out-of-sample factor estimates |
| `.oos_start_` | Index where OOS estimates begin |
| `.loadings_history_` | List of loading matrices per step |
| `.sharpe_weights_history_` | Max-Sharpe weights per step |

### Functions

| Function | Description |
|----------|-------------|
| `rppca_decompose(X, n_factors, gamma=10)` | Core decomposition (returns loadings, factors, eigenvalues) |
| `pca_decompose(X, n_factors)` | Standard PCA (γ=-1 shortcut) |
| `max_sharpe_ratio(factors)` | Maximum Sharpe ratio |
| `pricing_errors(X, factors)` | Per-asset alphas |
| `rms_pricing_error(X, factors)` | RMS pricing error |
| `idiosyncratic_variance(X, factors)` | Average unexplained variance |
| `explained_variation_ratio(X, factors)` | R² of the factor model |

### Utilities

```python
from rppca.utils import eigenvalue_ratio_test, variance_signal, eigenvalue_spectrum

# Suggest number of factors (Ahn & Horenstein, 2013)
n_factors, ratios = eigenvalue_ratio_test(X, max_factors=10, gamma=10)

# Variance signal diagnostic (strong vs weak factors)
signals = variance_signal(X, n_factors=5, gamma=10)

# Scree plot data
evals = eigenvalue_spectrum(X, gamma=10, n_top=10)
```

## Examples

Run the simulation example:

```bash
python scripts/example_simulation.py
```

Sample output:
```
1. IN-SAMPLE COMPARISON
  PCA (γ=-1)            |  Max SR: 0.0799  |  RMS α: 0.001088
  RP-PCA (γ=10)         |  Max SR: 0.5728  |  RMS α: 0.000715

4. LOOK-AHEAD BIAS CHECK
  In-sample Max SR:      0.5728  (uses future data — biased)
  Out-of-sample Max SR:  0.1528  (no look-ahead — unbiased)
```

## Citation

If you use this package in your research, please cite the original paper:

```bibtex
@article{lettau2020estimating,
  title={Estimating latent asset-pricing factors},
  author={Lettau, Martin and Pelger, Markus},
  journal={Journal of Econometrics},
  volume={218},
  number={1},
  pages={1--31},
  year={2020},
  publisher={Elsevier}
}
```

## License

MIT License
