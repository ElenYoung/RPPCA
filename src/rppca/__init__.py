"""
RPPCA - Risk-Premium PCA for Asset Pricing

A Python implementation of the Risk-Premium PCA (RP-PCA) method from:
Lettau, M. & Pelger, M. (2020). "Estimating latent asset-pricing factors."
Journal of Econometrics.

RP-PCA generalizes PCA by including a penalty term that accounts for pricing
errors in expected returns, enabling detection of weak factors with high
Sharpe ratios that standard PCA cannot find.
"""

from rppca.model import RPPCA, RollingRPPCA
from rppca.core import rppca_decompose, pca_decompose
from rppca.evaluation import (
    max_sharpe_ratio,
    pricing_errors,
    rms_pricing_error,
    idiosyncratic_variance,
    explained_variation_ratio,
)

__version__ = "0.1.0"

__all__ = [
    "RPPCA",
    "RollingRPPCA",
    "rppca_decompose",
    "pca_decompose",
    "max_sharpe_ratio",
    "pricing_errors",
    "rms_pricing_error",
    "idiosyncratic_variance",
    "explained_variation_ratio",
]
