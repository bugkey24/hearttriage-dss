"""Tests for helper utilities."""

import pandas as pd

from src.utils.helpers import triage_distribution


def test_distribution_sums_to_100():
    df = pd.DataFrame({"triage": ["P1 - Emergency"] * 3 + ["P3 - Non-Urgent"]})
    dist = triage_distribution(df)
    assert dist["percentage"].sum() == 100.0


def test_distribution_counts_match():
    df = pd.DataFrame({"triage": ["P2 - Urgent"] * 7 + ["P1 - Emergency"]})
    dist = triage_distribution(df)
    counts = dict(zip(dist["triage"], dist["count"]))
    assert counts["P2 - Urgent"] == 7
    assert counts["P1 - Emergency"] == 1


def test_distribution_columns():
    df = pd.DataFrame({"triage": ["P3 - Non-Urgent"]})
    dist = triage_distribution(df)
    assert list(dist.columns) == ["triage", "count", "percentage"]
