"""Tests for the categorical transformer."""

import pandas as pd

from src.config import CRITERIA, MAPPING
from src.data.cleaner import clean
from src.data.transformer import transform


def test_transform_applies_all_mappings(sample_df):
    result = transform(clean(sample_df))
    for col in MAPPING:
        assert set(result[col].dropna().tolist()) <= set(MAPPING[col].values())


def test_transform_sex_mapping(sample_df):
    result = transform(clean(sample_df))
    assert result["sex"].tolist() == [1, 1]  # male, male (third row dropped: missing '?')


def test_transform_unknown_value_raises_nan(sample_df):
    df = clean(sample_df)
    df.loc[0, "slope"] = "banana"  # not in mapping
    result = transform(df)
    assert pd.isna(result["slope"].iloc[0])


def test_transform_thal_values(sample_df):
    result = transform(clean(sample_df))
    assert result["thal"].tolist() == [6, 3]  # fix=6, norm=3


def test_transform_fully_numeric_criteria(sample_df):
    result = transform(clean(sample_df))
    for col in CRITERIA:
        assert pd.api.types.is_numeric_dtype(result[col]), col
