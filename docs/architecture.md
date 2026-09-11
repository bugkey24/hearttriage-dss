<div align="center">

# System Architecture

[![Docs](https://img.shields.io/badge/Docs-Architecture-blue?style=flat-square)](index.md)

</div>

HeartTriage DSS follows a classic three-layer Decision Support System
architecture: **Data → Application → Presentation**.

---

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ CLI Report   │  │ Notebook     │  │ Dashboard    │       │
│  │ (terminal)   │  │ (Colab/Jupy) │  │ (Streamlit)  │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  DSS Engine (SAW)                                    │   │
│  │  - Normalization                                     │   │
│  │  - Score Calculation                                 │   │
│  │  - Triage Categorization                             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────────┐
│                    DATA LAYER                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ Raw Data     │  │ Cleaning     │  │ Processed    │       │
│  │ cleve.mod    │→ │ Pipeline     │→ │ cleve_clean  │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Data Flow

```
cleve.mod
   │
   ▼
[1] Load & Parsing (whitespace delimiter)
   │
   ▼
[2] Assign Column Names
   │
   ▼
[3] Handle Missing Values (? → NaN → drop/impute)
   │
   ▼
[4] Convert Categorical → Numeric Scores
   │
   ▼
[5] Normalize Decision Matrix (benefit/cost)
   │
   ▼
[6] SAW Score Calculation
   │
   ▼
[7] Triage Categorization (P1/P2/P3)
   │
   ▼
[8] Output: Table + Visualization + Recommendation
```

---

## 3. Modular Components

| Module | Path | Function |
|--------|------|----------|
| `config.py` | `src/config.py` | Central configuration (weights, thresholds, mappings) |
| `loader.py` | `src/data/loader.py` | Read `cleve.mod` |
| `cleaner.py` | `src/data/cleaner.py` | Clean the data |
| `transformer.py` | `src/data/transformer.py` | Convert categorical values |
| `saw.py` | `src/dss/saw.py` | Implement SAW |
| `triage.py` | `src/dss/triage.py` | Categorize triage |
| `plots.py` | `src/visualization/plots.py` | Visualize results |
| `logger.py` | `src/utils/logger.py` | Logging utilities |
| `helpers.py` | `src/utils/helpers.py` | Shared helpers |

---

## 4. Design Principles

1. **Separation of concerns** — data, decision logic, and presentation are independent layers.
2. **Configuration over hard-coding** — all weights & thresholds live in `src/config.py`.
3. **Pure functions** — pipeline stages take a DataFrame in, return a DataFrame out; easy to test.
4. **Dual execution** — the same logic runs locally (modular `src/`) or in Colab (self-contained inline).

---

## 5. Scalability Considerations

| Aspect | Current | Future |
|--------|---------|--------|
| **Data size** | 303 rows | 10k+ rows |
| **Storage** | CSV/Parquet | Database (PostgreSQL) |
| **Compute** | Single machine | Distributed (Spark) |
| **Serving** | CLI/Notebook | REST API (FastAPI) |
| **UI** | Streamlit | React + FastAPI |

---

*Related: [Pipeline](pipeline.md) · [Methodology](methodology.md) · [User Guide](user_guide.md)*
