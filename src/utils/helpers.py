"""Shared helper functions."""

import pandas as pd


def triage_distribution(df: pd.DataFrame, triage_col: str = "triage") -> pd.DataFrame:
    """Compute triage category counts and percentages.

    Returns:
        DataFrame with columns: triage, count, percentage.
    """
    counts = df[triage_col].value_counts().reset_index()
    counts.columns = ["triage", "count"]
    counts["percentage"] = (counts["count"] / counts["count"].sum() * 100).round(1)
    return counts
