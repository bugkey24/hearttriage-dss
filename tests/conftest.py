# isort: skip_file
"""Shared pytest fixtures and sys.path bootstrap for the test suite."""

import io
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.config import COLUMNS  # noqa: E402

RAW_SAMPLE = """\
63.0 male angina 145.0 233.0 true  hyp 150.0 fal  2.3 down 0.0  fix buff  H
67.0 male asympt 160.0 286.0 fal   hyp 108.0 true 1.5 flat 3.0 norm sick S2
53.0  fem notang 128.0 216.0 fal   hyp 115.0 fal  0.0   up  ?  norm buff  H
"""


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Small raw-format sample mimicking cleve.mod structure (row 3 has '?')."""
    return pd.read_csv(io.StringIO(RAW_SAMPLE), sep=r"\s+", header=None, names=COLUMNS, comment="%")
