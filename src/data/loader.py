"""Raw data loader for cleve.mod."""

import pandas as pd

from src.config import COLUMNS


def load_raw(path: str) -> pd.DataFrame:
    """Load cleve.mod with whitespace delimiter.

    Args:
        path: Path to the raw dataset file.

    Returns:
        DataFrame with named columns (303 x 15 expected).
    """
    df = pd.read_csv(path, sep=r"\s+", header=None, names=COLUMNS, comment="%")
    return df
