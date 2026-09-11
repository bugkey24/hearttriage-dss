"""Generate all standard figures from processed triage data."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from src.config import CRITERIA, TRIAGE_DATA_PATH
from src.utils.logger import get_logger
from src.visualization.plots import (
    plot_correlation,
    plot_radar_p1,
    plot_scatter,
    plot_score_boxplot,
    plot_score_histogram,
    plot_triage_distribution,
)

logger = get_logger(__name__)

FIGURES_DIR = Path("outputs/figures")


def generate_all_figures(df: pd.DataFrame) -> list[Path]:
    """Render every standard plot into outputs/figures/ and return the paths."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    figures = [
        (
            FIGURES_DIR / "triage_distribution.png",
            lambda: plot_triage_distribution(df, FIGURES_DIR / "triage_distribution.png"),
        ),
        (
            FIGURES_DIR / "correlation.png",
            lambda: plot_correlation(df, CRITERIA, FIGURES_DIR / "correlation.png"),
        ),
        (
            FIGURES_DIR / "score_boxplot.png",
            lambda: plot_score_boxplot(df, FIGURES_DIR / "score_boxplot.png"),
        ),
        (FIGURES_DIR / "scatter.png", lambda: plot_scatter(df, FIGURES_DIR / "scatter.png")),
        (
            FIGURES_DIR / "score_histogram.png",
            lambda: plot_score_histogram(df, FIGURES_DIR / "score_histogram.png"),
        ),
        (
            FIGURES_DIR / "radar_p1.html",
            lambda: plot_radar_p1(df, CRITERIA, FIGURES_DIR / "radar_p1.html"),
        ),
    ]

    written = []
    for path, render in figures:
        render()
        written.append(path)
        logger.info(f"  saved {path}")
    return written


def main() -> None:
    if not Path(TRIAGE_DATA_PATH).exists():
        logger.error("Run `python scripts/run_pipeline.py` first to produce triage data.")
        sys.exit(1)

    df = pd.read_csv(TRIAGE_DATA_PATH)
    logger.info("Generating figures...")
    generate_all_figures(df)
    logger.info(f"Done. {len(list(FIGURES_DIR.iterdir()))} files in {FIGURES_DIR}")


if __name__ == "__main__":
    main()
