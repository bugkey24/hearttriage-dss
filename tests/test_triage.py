"""Tests for triage classification."""

import pandas as pd

from src.config import THRESHOLDS, TRIAGE_LABELS
from src.dss.triage import classify_triage


def test_classify_p1():
    scores = pd.Series([0.70, 0.90])
    result = classify_triage(scores, THRESHOLDS, TRIAGE_LABELS)
    assert (result == "P1 - Emergency").all()


def test_classify_p2():
    scores = pd.Series([0.45, 0.55, 0.6499])
    result = classify_triage(scores, THRESHOLDS, TRIAGE_LABELS)
    assert (result == "P2 - Urgent").all()


def test_classify_p3():
    scores = pd.Series([0.10, 0.44])
    result = classify_triage(scores, THRESHOLDS, TRIAGE_LABELS)
    assert (result == "P3 - Non-Urgent").all()


def test_classify_boundaries():
    scores = pd.Series([0.65, 0.45, 0.4499])
    result = classify_triage(scores, THRESHOLDS, TRIAGE_LABELS).tolist()
    assert result == ["P1 - Emergency", "P2 - Urgent", "P3 - Non-Urgent"]
