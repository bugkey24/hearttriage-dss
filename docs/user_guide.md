<div align="center">

# User Guide

[![Docs](https://img.shields.io/badge/Docs-User%20Guide-blue?style=flat-square)](index.md)
[![Colab](https://img.shields.io/badge/Run%20in-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab)](../colab/HeartTriage_DSS_Colab.ipynb)

</div>

---

## 1. Prerequisites

- Python **3.10+**
- Git (for local mode)
- A Google account (for Colab mode)

---

## 2. Local Mode (Native)

### Setup

```bash
# 1. Clone repo
git clone https://github.com/bugkey24/hearttriage-dss.git
cd hearttriage-dss

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run pipeline
python scripts/run_pipeline.py

# 5. Or run notebooks
jupyter notebook notebooks/
```

### Available Scripts

| Script | Function |
|--------|----------|
| `scripts/run_pipeline.py` | Full pipeline: load → clean → transform → SAW → triage |
| `scripts/run_triage.py` | Triage scoring only (uses processed data) |
| `scripts/generate_report.py` | Generate HTML report |

### Using Make

```bash
make install   # install dependencies
make run       # run full pipeline
make test      # run test suite
make clean     # remove generated outputs
```

---

## 3. Google Colab Mode

**Strategy:** a **self-contained** notebook that does not depend on the repo structure.

### Option A: Self-contained notebook (recommended)

1. Open [`colab/HeartTriage_DSS_Colab.ipynb`](../colab/HeartTriage_DSS_Colab.ipynb) in Google Colab
2. Upload `cleve.mod` when prompted
3. Run all cells — results appear inline

### Option B: Clone the repo in Colab

```python
!git clone https://github.com/bugkey24/hearttriage-dss.git
%cd hearttriage-dss
!pip install -r requirements.txt -q

from src.data.loader import load_raw
from src.data.cleaner import clean
from src.data.transformer import transform
from src.dss.saw import normalize, calculate_score
from src.dss.triage import classify_triage

df = load_raw('data/raw/cleve.mod')
df = clean(df)
df = transform(df)
# ... etc
```

### Option C: Mount Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/hearttriage-dss
```

---

## 4. Dual Mode Comparison

| Aspect | Local | Colab |
|--------|-------|-------|
| **Setup** | Manual (venv) | Automatic |
| **Data** | Local file | Upload/Drive |
| **Modularity** | Full (`src/`) | Inline/simple |
| **Reproducibility** | High | Medium |
| **Portability** | Limited | High |
| **Best for** | Development | Demo/Assignment |

---

## 5. Understanding the Output

### Triage Results Table

| Patient | Age | Trestbps | Chol | Thalach | Oldpeak | Score | Triage |
|---------|----:|---------:|-----:|--------:|--------:|------:|--------|
| 1 | 63 | 145 | 233 | 150 | 2.3 | 0.72 | P1 |
| 2 | 67 | 160 | 286 | 108 | 1.5 | 0.68 | P1 |
| 3 | 37 | 130 | 250 | 187 | 3.5 | 0.41 | P3 |

### Triage Distribution

| Triage | Count | Percentage |
|--------|------:|-----------:|
| P1 | 45 | 15.2% |
| P2 | 120 | 40.4% |
| P3 | 132 | 44.4% |

### Output Files

| Path | Content |
|------|---------|
| `data/interim/cleve_interim.csv` | Data after cleaning |
| `data/processed/cleve_clean.csv` | Clean data |
| `data/processed/cleve_triage.csv` | Data + triage results |
| `outputs/figures/` | PNG/HTML visualizations |
| `outputs/reports/triage_report.html` | HTML report |
| `outputs/logs/` | Execution logs |

---

## 6. Troubleshooting

| Problem | Solution |
|---------|----------|
| `FileNotFoundError: cleve.mod` | Ensure dataset is at `data/raw/cleve.mod` |
| `ModuleNotFoundError: src` | Run scripts from repo root, or `pip install -e .` |
| Colab upload fails | Re-run the upload cell; check file is `cleve.mod` (not `.csv`) |
| Windows activation error | Use `.venv\Scripts\activate` in PowerShell/cmd |

---

*Related: [Pipeline](pipeline.md) · [Architecture](architecture.md)*
