<div align="center">

# Data Processing Pipeline

[![Stages](https://img.shields.io/badge/Stages-6-blue?style=flat-square)](index.md)

</div>

The pipeline transforms raw `cleve.mod` into triage results in 6 stages.
Each stage is a pure function: DataFrame in → DataFrame out.

---

## Stage 1: Data Loading

```python
# src/data/loader.py
import pandas as pd

COLUMNS = ['age','sex','cp','trestbps','chol','fbs','restecg',
           'thalach','exang','oldpeak','slope','ca','thal',
           'class','subclass']

def load_raw(path: str) -> pd.DataFrame:
    """Load cleve.mod with whitespace delimiter."""
    df = pd.read_csv(path, sep=r'\s+', header=None, names=COLUMNS)
    return df
```

**Output:** DataFrame 303×15

---

## Stage 2: Data Cleaning

```python
# src/data/cleaner.py
import numpy as np
import pandas as pd

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data: missing values, duplicates, data types."""
    df = df.copy()

    # 1. Replace '?' with NaN
    df.replace('?', np.nan, inplace=True)

    # 2. Convert numeric columns
    num_cols = ['age','trestbps','chol','thalach','oldpeak','ca']
    df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')

    # 3. Drop rows with missing values
    df.dropna(inplace=True)

    # 4. Drop duplicates
    df.drop_duplicates(inplace=True)

    # 5. Reset index
    df.reset_index(drop=True, inplace=True)

    return df
```

**Output:** Clean DataFrame (± 297 rows)

---

## Stage 3: Data Transformation

```python
# src/data/transformer.py
import pandas as pd

MAPPING = {
    'sex': {'male': 1, 'fem': 0},
    'cp': {'angina': 1, 'abnang': 2, 'notang': 3, 'asympt': 4},
    'fbs': {'true': 1, 'fal': 0},
    'restecg': {'norm': 0, 'abn': 1, 'hyp': 2},
    'exang': {'true': 1, 'fal': 0},
    'slope': {'up': 1, 'flat': 2, 'down': 3},
    'thal': {'norm': 3, 'fixed': 6, 'fix': 6, 'rev': 7}
}

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Convert categorical values to numeric scores."""
    df = df.copy()
    for col, mapping in MAPPING.items():
        df[col] = df[col].map(mapping)
    return df
```

**Output:** Fully numeric DataFrame

---

## Stage 4: SAW Normalization & Scoring

```python
# src/dss/saw.py
import pandas as pd

def normalize(df: pd.DataFrame, criteria: list, benefit: list) -> pd.DataFrame:
    """Normalize the decision matrix."""
    norm = df[criteria].copy()
    cost = [c for c in criteria if c not in benefit]

    for c in benefit:
        norm[c] = df[c] / df[c].max()
    for c in cost:
        norm[c] = df[c].min() / df[c]

    return norm

def calculate_score(norm: pd.DataFrame, weights: dict) -> pd.Series:
    """Calculate the SAW score."""
    return sum(norm[c] * weights[c] for c in norm.columns)
```

**Output:** Normalized matrix + score

---

## Stage 5: Triage Categorization

```python
# src/dss/triage.py
import pandas as pd

def classify_triage(scores: pd.Series, thresholds: dict) -> pd.Series:
    """Categorize scores into P1/P2/P3."""
    def kategori(s):
        if s >= thresholds['P1']:
            return 'P1 - Emergency'
        elif s >= thresholds['P2']:
            return 'P2 - Urgent'
        else:
            return 'P3 - Non-Urgent'
    return scores.apply(kategori)
```

**Output:** `triage` + `recommendation` columns

---

## Stage 6: Output & Reporting

```python
# scripts/generate_report.py
def generate_report(df: pd.DataFrame, output_path: str):
    """Generate HTML/PDF report."""
    # ... template rendering (Jinja2) ...
    pass
```

**Output:** `outputs/reports/triage_report.html`

---

## Storage & Efficiency

| Format | Size | Notes |
|--------|-----:|-------|
| `.mod` (raw) | ~25 KB | Original format |
| `.csv` | ~30 KB | Readable, universal |
| `.parquet` | ~15 KB | Compressed, fast |
| `.feather` | ~15 KB | Fast for pandas |

> **Recommendation:** Parquet for production, CSV for debugging.

| Optimization | Technique |
|--------------|-----------|
| **Vectorization** | Use pandas/numpy, avoid loops |
| **Caching** | Store normalization results |
| **Dtype optimization** | `int8` for categories, `float32` for numerics |
| **Chunking** | For large data (not needed here) |

Total runtime estimate: **< 3 s** for the full pipeline (303 rows).

---

*Related: [Architecture](architecture.md) · [Methodology](methodology.md)*
