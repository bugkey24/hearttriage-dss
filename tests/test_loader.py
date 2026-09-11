"""Tests for the raw data loader."""

import pandas as pd

from src.config import COLUMNS, RAW_DATA_PATH
from src.data.loader import load_raw


def test_load_raw_real_dataset():
    df = load_raw(RAW_DATA_PATH)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == COLUMNS
    assert len(df) >= 300


def test_load_raw_skips_comment_header():
    df = load_raw(RAW_DATA_PATH)
    # Header comments contain '%'; first data row should start with age 63.0
    assert float(df.iloc[0]["age"]) == 63.0
