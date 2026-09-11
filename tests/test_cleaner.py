"""Tests for the data cleaner."""

import pandas as pd

from src.data.cleaner import clean


def test_clean_replaces_missing(sample_df):
    cleaned = clean(sample_df)
    assert not cleaned.isin(["?"]).any().any()


def test_clean_drops_rows_with_missing(sample_df):
    cleaned = clean(sample_df)
    # Row 3 has '?' in 'ca' -> dropped
    assert len(cleaned) == 2
    assert cleaned.isna().sum().sum() == 0


def test_clean_numeric_dtypes(sample_df):
    cleaned = clean(sample_df)
    for col in ["age", "trestbps", "chol", "thalach", "oldpeak", "ca"]:
        assert pd.api.types.is_numeric_dtype(cleaned[col])


def test_clean_preserves_original(sample_df):
    original = sample_df.copy()
    clean(sample_df)
    # '?' should still exist in the original
    assert original.isin(["?"]).any().any()
