"""Generate an HTML triage report using a Jinja2 template."""

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.config import TRIAGE_ACTIONS, TRIAGE_DATA_PATH
from src.utils.helpers import triage_distribution
from src.utils.logger import get_logger

logger = get_logger(__name__)

TEMPLATE_DIR = Path("templates")
REPORT_PATH = Path("outputs/reports/triage_report.html")


def generate_report(df: pd.DataFrame, output_path: Path = REPORT_PATH) -> Path:
    """Render triage results into an HTML report."""
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=select_autoescape(["html"]))
    template = env.get_template("report.html")

    dist = triage_distribution(df)
    dist["action"] = dist["triage"].str[:2].map(TRIAGE_ACTIONS)

    html = template.render(
        date=date.today().isoformat(),
        total=len(df),
        distribution=dist.to_dict("records"),
        preview=df[["age", "score", "triage"]].head(20).to_dict("records"),
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    logger.info(f"Report saved to {output_path}")
    return output_path


def main() -> None:
    if not Path(TRIAGE_DATA_PATH).exists():
        logger.error("Run `python scripts/run_pipeline.py` first.")
        return
    df = pd.read_csv(TRIAGE_DATA_PATH)
    generate_report(df)


if __name__ == "__main__":
    main()
