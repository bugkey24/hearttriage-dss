"""Run the full HeartTriage DSS pipeline."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from src.config import (
    BENEFIT,
    CRITERIA,
    PROCESSED_DATA_PATH,
    RAW_DATA_PATH,
    THRESHOLDS,
    TRIAGE_DATA_PATH,
    TRIAGE_LABELS,
    WEIGHTS,
)
from src.data.cleaner import clean
from src.data.loader import load_raw
from src.data.transformer import transform
from src.dss.saw import calculate_score, normalize
from src.dss.triage import classify_triage
from src.utils.helpers import triage_distribution
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_pipeline() -> pd.DataFrame:
    """Execute all stages and return the final triage DataFrame."""
    logger.info("[1/6] Loading raw data...")
    df = load_raw(RAW_DATA_PATH)
    logger.info(f"Loaded {len(df)} rows x {df.shape[1]} cols")

    logger.info("[2/6] Cleaning data...")
    df = clean(df)
    logger.info(f"{len(df)} rows remaining")
    df.to_csv("data/interim/cleve_interim.csv", index=False)

    logger.info("[3/6] Transforming categoricals...")
    df = transform(df)

    logger.info("[4/6] SAW normalization & scoring...")
    norm = normalize(df, CRITERIA, BENEFIT)
    df["score"] = calculate_score(norm, WEIGHTS).round(4)

    logger.info("[5/6] Triage categorization...")
    df["triage"] = classify_triage(df["score"], THRESHOLDS, TRIAGE_LABELS)

    logger.info("[6/6] Saving outputs...")
    Path(PROCESSED_DATA_PATH).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(TRIAGE_DATA_PATH, index=False)

    dist = triage_distribution(df)
    logger.info("Triage distribution:\n%s", dist.to_string(index=False))
    logger.info(f"Done. Results saved to {TRIAGE_DATA_PATH}")
    return df


if __name__ == "__main__":
    run_pipeline()
