"""SAW (Simple Additive Weighting) engine."""

import numpy as np
import pandas as pd


def normalize(df: pd.DataFrame, criteria: list, benefit: list) -> pd.DataFrame:
    """Normalize the decision matrix (benefit/cost).

    Args:
        df: Numeric DataFrame containing criteria columns.
        criteria: List of criterion column names.
        benefit: Subset of criteria treated as benefit (higher = better).

    Returns:
        Normalized decision matrix (values in 0-1 range).
    """
    norm = df[criteria].copy()
    cost = [c for c in criteria if c not in benefit]

    for c in benefit:
        norm[c] = df[c] / df[c].max()
    for c in cost:
        cmin = df[c].min()
        # Guard zero-division: the minimum itself normalizes to 1.0
        norm[c] = np.where(df[c] == cmin, 1.0, cmin / df[c])

    return norm


def calculate_score(norm: pd.DataFrame, weights: dict) -> pd.Series:
    """Calculate the SAW weighted score.

    Args:
        norm: Normalized decision matrix.
        weights: Mapping of criterion name to weight (sums to 1.0).

    Returns:
        Series of final scores V_i (one per patient).
    """
    return sum(norm[c] * weights[c] for c in norm.columns)
