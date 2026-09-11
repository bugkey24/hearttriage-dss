"""End-to-end integration test on the real dataset."""

from src.config import (
    BENEFIT,
    CRITERIA,
    RAW_DATA_PATH,
    THRESHOLDS,
    TRIAGE_LABELS,
    WEIGHTS,
)
from src.data.cleaner import clean
from src.data.loader import load_raw
from src.data.transformer import transform
from src.dss.saw import calculate_score, normalize
from src.dss.triage import classify_triage


def test_full_pipeline():
    df = load_raw(RAW_DATA_PATH)
    assert 300 <= len(df) <= 310

    df = clean(df)
    assert 290 <= len(df) < 300
    assert df.isna().sum().sum() == 0

    df = transform(df)
    assert df[CRITERIA].isna().sum().sum() == 0

    norm = normalize(df, CRITERIA, BENEFIT)
    df["score"] = calculate_score(norm, WEIGHTS)
    assert df["score"].between(0, 1).all()

    df["triage"] = classify_triage(df["score"], THRESHOLDS, TRIAGE_LABELS)
    assert set(df["triage"].unique()) <= set(TRIAGE_LABELS.values())
    assert not df["triage"].empty

    # Distribution sanity: all three categories represented
    assert df["triage"].nunique() == 3

    # SAW scores must strictly decrease across triage levels by construction
    means = df.groupby("triage")["score"].mean()
    assert means[TRIAGE_LABELS["P1"]] > means[TRIAGE_LABELS["P2"]] > means[TRIAGE_LABELS["P3"]]
