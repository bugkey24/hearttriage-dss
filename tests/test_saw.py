"""Tests for the SAW engine."""

import numpy as np
import pandas as pd
import pytest

from src.config import BENEFIT, CRITERIA, WEIGHTS
from src.dss.saw import calculate_score, normalize


@pytest.fixture
def numeric_df():
    return pd.DataFrame(
        {
            "age": [63.0, 67.0, 37.0],
            "trestbps": [145.0, 160.0, 130.0],
            "chol": [233.0, 286.0, 250.0],
            "thalach": [150.0, 108.0, 187.0],
            "oldpeak": [2.3, 1.5, 3.5],
            "ca": [0.0, 3.0, 0.0],
            "thal": [6, 3, 3],
            "exang": [0, 1, 0],
        }
    )


def test_normalize_in_zero_one(numeric_df):
    norm = normalize(numeric_df, CRITERIA, BENEFIT)
    assert ((norm >= 0) & (norm <= 1)).all().all()


def test_normalize_benefit(numeric_df):
    norm = normalize(numeric_df, CRITERIA, BENEFIT)
    # Benefit: max value normalizes to 1.0
    assert np.isclose(norm["thalach"].max(), 1.0)


def test_normalize_cost(numeric_df):
    norm = normalize(numeric_df, CRITERIA, BENEFIT)
    # Cost: min value normalizes to 1.0
    assert np.isclose(norm["age"].max(), 1.0)


def test_calculate_score_sums_weights(numeric_df):
    norm = normalize(numeric_df, CRITERIA, BENEFIT)
    scores = calculate_score(norm, WEIGHTS)
    assert len(scores) == len(numeric_df)
    assert scores.between(0, 1).all()


def test_calculate_score_identical_patient(numeric_df):
    # A patient with all-min cost and max benefit values scores 1.0
    best = numeric_df.iloc[[numeric_df["thalach"].idxmax()]].copy()
    for c in CRITERIA:
        if c != "thalach":
            best[c] = numeric_df[c].min()
    norm = normalize(best, CRITERIA, BENEFIT)
    scores = calculate_score(norm, WEIGHTS)
    assert np.isclose(scores.iloc[0], 1.0)
