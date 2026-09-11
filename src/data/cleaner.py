"""Data cleaning utilities."""

import numpy as np
import pandas as pd

from src.config import MISSING_MARKER, NUMERIC_COLUMNS


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data: missing values, duplicates, data types.

    Args:
        df: Raw DataFrame loaded from cleve.mod.

    Returns:
        Cleaned DataFrame with missing rows dropped.
    """
    df = df.copy()

    # 1. Replace '?' with NaN
    df.replace(MISSING_MARKER, np.nan, inplace=True)

    # 2. Convert numeric columns
    df[NUMERIC_COLUMNS] = df[NUMERIC_COLUMNS].apply(pd.to_numeric, errors="coerce")

    # 3. Drop rows with missing values
    df.dropna(inplace=True)

    # 4. Drop duplicates
    df.drop_duplicates(inplace=True)

    # 5. Reset index
    df.reset_index(drop=True, inplace=True)

    return df
