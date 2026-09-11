"""Tests for central configuration validity."""

import numpy as np

from src.config import BENEFIT, COLUMNS, COST, CRITERIA, THRESHOLDS, WEIGHTS


def test_weights_sum_to_one():
    assert np.isclose(sum(WEIGHTS.values()), 1.0)


def test_weights_cover_all_criteria():
    assert set(WEIGHTS.keys()) == set(CRITERIA)


def test_benefit_and_cost_partition_criteria():
    assert set(BENEFIT) | set(COST) == set(CRITERIA)
    assert not set(BENEFIT) & set(COST)


def test_thresholds_are_monotonic():
    assert THRESHOLDS["P1"] > THRESHOLDS["P2"]


def test_columns_are_unique():
    assert len(COLUMNS) == len(set(COLUMNS)) == 15
