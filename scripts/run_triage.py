"""Run triage scoring on already-processed data."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from src.config import TRIAGE_DATA_PATH
from src.utils.helpers import triage_distribution
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main() -> pd.DataFrame | None:
    """Display triage summary from processed data."""
    if not Path(TRIAGE_DATA_PATH).exists():
        logger.error(f"{TRIAGE_DATA_PATH} not found. Run `python scripts/run_pipeline.py` first.")
        return None

    df = pd.read_csv(TRIAGE_DATA_PATH)
    dist = triage_distribution(df)
    logger.info("Triage distribution:\n%s", dist.to_string(index=False))
    logger.info("\n%s", df[["age", "score", "triage"]].head(10).to_string(index=False))
    return df


if __name__ == "__main__":
    main()
