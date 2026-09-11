"""Categorical-to-numeric transformation."""

import pandas as pd

from src.config import MAPPING


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Convert categorical values to numeric scores.

    Args:
        df: Cleaned DataFrame.

    Returns:
        Fully numeric DataFrame ready for SAW normalization.
    """
    df = df.copy()
    for col, mapping in MAPPING.items():
        df[col] = df[col].map(mapping)
    return df
