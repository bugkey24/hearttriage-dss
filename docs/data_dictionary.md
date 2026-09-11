<div align="center">

# Data Dictionary — Cleveland Heart Disease Dataset

[![Dataset](https://img.shields.io/badge/Source-UCI%20ML%20Repository-9B59B6?style=flat-square)](https://archive.ics.uci.edu/dataset/45/heart+disease)
[![Rows](https://img.shields.io/badge/Rows-303-informational?style=flat-square)]()
[![Columns](https://img.shields.io/badge/Columns-15-informational?style=flat-square)]()

</div>

---

## 1. Data Source

| Attribute | Value |
|-----------|-------|
| **File name** | `data/raw/cleve.mod` |
| **Source** | UCI Machine Learning Repository — Cleveland Heart Disease Dataset |
| **Modification** | Dr. Detrano (1990), adapted into a mixed dataset |
| **Number of rows** | ± 303 |
| **Number of columns** | 15 (13 features + 1 class + 1 subclass) |

---

## 2. Attribute Structure

| No | Attribute | Type | Values | Description |
|----|-----------|------|--------|-------------|
| 1 | `age` | Numeric | 29–77 | Patient age (years) |
| 2 | `sex` | Symbolic | male/fem | Gender |
| 3 | `cp` | Symbolic | angina, abnang, notang, asympt | Chest pain type |
| 4 | `trestbps` | Numeric | 94–200 | Resting blood pressure (mm Hg) |
| 5 | `chol` | Numeric | 126–564 | Serum cholesterol (mg/dl) |
| 6 | `fbs` | Symbolic | true/fal | Fasting blood sugar > 120 mg/dl |
| 7 | `restecg` | Symbolic | norm, abn, hyp | Resting ECG result |
| 8 | `thalach` | Numeric | 71–202 | Maximum heart rate achieved |
| 9 | `exang` | Symbolic | true/fal | Exercise-induced angina |
| 10 | `oldpeak` | Numeric | 0–6.2 | ST depression induced by exercise |
| 11 | `slope` | Symbolic | up, flat, down | Slope of ST segment |
| 12 | `ca` | Numeric | 0–3, `?` | Number of major vessels colored |
| 13 | `thal` | Symbolic | norm, fixed, rev, `?` | Thalassemia |
| 14 | `class` | Symbolic | buff/sick | Diagnosis |
| 15 | `subclass` | Symbolic | H, S1–S4 | Diagnosis subtype |

---

## 3. Data Characteristics

- **Mixed dataset:** combination of numeric & categorical.
- **Missing values:** `?` present in `ca` and `thal` (± 6 rows).
- **Format inconsistency:** double spaces on some rows.
- **Class distribution:** ± 164 `buff`, ± 139 `sick` (relatively balanced).
- **Outliers:** present in `chol` (564) and `oldpeak` (6.2).

---

## 4. Descriptive Statistics

| Statistic | age | trestbps | chol | thalach | oldpeak |
|-----------|----:|---------:|-----:|--------:|--------:|
| Mean | 54.4 | 131.7 | 246.7 | 149.6 | 1.04 |
| Std | 9.0 | 17.6 | 51.8 | 22.9 | 1.16 |
| Min | 29 | 94 | 126 | 71 | 0 |
| Max | 77 | 200 | 564 | 202 | 6.2 |

---

## 5. Column Name Constant

```python
COLUMNS = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal',
    'class', 'subclass'
]
```

---

## 6. Derived Columns (after pipeline)

| Column | Content | Produced by |
|--------|---------|-------------|
| `score` | SAW final score (0–1) | `src/dss/saw.py` |
| `triage` | P1/P2/P3 category | `src/dss/triage.py` |
| `recommendation` | Action recommendation | `src/dss/triage.py` |

---

*Related: [Methodology](methodology.md) · [Pipeline](pipeline.md) · [References](references.md)*
