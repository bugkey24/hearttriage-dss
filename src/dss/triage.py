"""Triage categorization from SAW scores."""

import pandas as pd


def classify_triage(scores: pd.Series, thresholds: dict, labels: dict) -> pd.Series:
    """Categorize scores into P1/P2/P3.

    Args:
        scores: SAW final scores per patient.
        thresholds: Dict with 'P1' and 'P2' cutoff values.
        labels: Dict mapping category code to display label.

    Returns:
        Series of triage labels.
    """

    def kategori(s: float) -> str:
        if s >= thresholds["P1"]:
            return labels["P1"]
        elif s >= thresholds["P2"]:
            return labels["P2"]
        else:
            return labels["P3"]

    return scores.apply(kategori)
