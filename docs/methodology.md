<div align="center">

# DSS Methodology — SAW

[![Method](https://img.shields.io/badge/Method-Simple%20Additive%20Weighting-2ECC71?style=flat-square)](index.md)

</div>

This document explains the **SAW (Simple Additive Weighting)** method used by
HeartTriage DSS to convert clinical profiles into triage decisions.

---

## 1. Overview

SAW is a Multi-Attribute Decision Making (MADM) technique that computes a
weighted sum of normalized criteria values for each alternative (patient):

```
V_i = Σ (w_j × r_ij)
```

Where:

- `V_i` = final score of alternative i (patient)
- `w_j` = weight of criterion j
- `r_ij` = normalized value of criterion j for patient i

---

## 2. Normalization Formulas

Because criteria use different units and scales, values must be normalized:

| Type | Formula | Meaning |
|------|---------|---------|
| **Benefit** | `r_ij = x_ij / max(x_j)` | Higher value = better |
| **Cost** | `r_ij = min(x_j) / x_ij` | Lower value = better |

---

## 3. Criteria & Weights

Criteria are selected based on **acute triage relevance**:

| Criterion | Type | Weight | Rationale |
|-----------|------|-------:|-----------|
| `age` | Cost | 0.10 | Older age = higher risk |
| `trestbps` | Cost | 0.15 | Hypertension = acute risk |
| `chol` | Cost | 0.10 | High cholesterol = risk |
| `thalach` | Benefit | 0.15 | Low max HR = poor |
| `oldpeak` | Cost | 0.15 | ST depression = ischemia |
| `ca` | Cost | 0.15 | Blocked vessels |
| `thal` | Cost | 0.10 | Thalassemia disorder |
| `exang` | Cost | 0.10 | Exercise angina |

**Total weight = 1.00**

>  These values are configured in `src/config.py` — never hard-code them.

---

## 4. Triage Categorization Thresholds

| Score | Category | Action |
|-------|----------|--------|
| ≥ 0.65 | **P1** — Emergency | Immediate treatment (< 5 minutes) |
| 0.45 – 0.65 | **P2** — Urgent | Fast treatment (< 30 minutes) |
| < 0.45 | **P3** — Non-Urgent | Can wait (< 60 minutes) |

> **Note:** Thresholds can be recalibrated based on clinical validation.

---

## 5. Categorical-to-Score Mapping

| Attribute | Mapping |
|-----------|---------|
| `sex` | male=1, fem=0 |
| `cp` | angina=1, abnang=2, notang=3, asympt=4 |
| `fbs` | true=1, fal=0 |
| `restecg` | norm=0, abn=1, hyp=2 |
| `exang` | true=1, fal=0 |
| `slope` | up=1, flat=2, down=3 |
| `thal` | norm=3, fixed/fix=6, rev=7 |

---

## 6. Decision Flow

```
┌──────────────────┐
│  Patient Input   │
│  (Clinical Data) │
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Data Cleaning   │
│  & Transformation│
└────────┬─────────┘
         ▼
┌──────────────────┐
│  SAW Normalization│
│  (Benefit/Cost)  │
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Weighted Score  │
│  Calculation     │
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Triage Category │
│  (P1 / P2 / P3)  │
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Recommendation  │
│  to Decision-    │
│  Maker           │
└──────────────────┘
```

---

## 7. Worked Example

Patient: age=63, trestbps=145, chol=233, thalach=150, oldpeak=2.3, ca=0, thal=fixed, exang=fal

1. Each criterion is normalized (benefit or cost formula above)
2. Each normalized value is multiplied by its weight
3. The weighted values are summed → **V = 0.72**
4. 0.72 ≥ 0.65 → **P1 — Emergency** 

---

## 8. References

- Fishburn, P.C. (1967). _Additive Utilities with Incomplete Product Sets._
- Hwang, C.L., & Yoon, K. (1981). _Multiple Attribute Decision Making._

*Related: [Data Dictionary](data_dictionary.md) · [Pipeline](pipeline.md) · [Glossary](glossary.md)*
