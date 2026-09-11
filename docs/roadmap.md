<div align="center">

# Development Roadmap

[![Status](https://img.shields.io/badge/Status-Released%20v1.0.0-success?style=flat-square)](https://github.com/bugkey24/hearttriage-dss/releases)
[![Phases](https://img.shields.io/badge/Phases-9%2F9-complete-success?style=flat-square)](#milestones)

</div>

---

## Milestones

| Phase | Milestone | Status |
|:-----:|-----------|:------:|
| 0 | Project setup & documentation | Done |
| 1 | Data understanding & cleaning | Done |
| 2 | SAW implementation | Done |
| 3 | Triage categorization | Done |
| 4 | Visualization | Done |
| 5 | Local pipeline | Done |
| 6 | Colab notebook | Done |
| 7 | Documentation (full) | Done |
| 8 | Testing | Done |
| 9 | Release v1.0.0 | Done |

**Legend:** Done > In progress > Not started

---

## Phase Details

### Phase 0 - Project Setup (Done)

- [x] Repository structure created
- [x] Documentation split into modular `docs/` files
- [x] README, CHANGELOG, CONTRIBUTING, LICENSE added
- [x] CI workflow configured (`pyproject.toml`, `.flake8` lint configs included)
- [x] Git repository initialized and pushed to `github.com/bugkey24/hearttriage-dss`

### Phase 1 - Data Understanding & Cleaning (Done)

- [x] `HT_01_data_understanding.ipynb`
- [x] `HT_02_data_cleaning.ipynb`
- [x] `src/data/loader.py`, `src/data/cleaner.py`
- [x] Unit tests

> **Bug fixed during testing:** the dataset token for thalassemia is `fix`
> (18 rows), not `fixed` as in the original spec — mapping corrected in
> `src/config.py` so all criteria resolve without NaN.

### Phase 2 - SAW Implementation (Done)

- [x] `src/dss/saw.py` (normalization + scoring, zero-division safe)
- [x] `HT_04_saw_implementation.ipynb` (incl. manual walkthrough)
- [x] Unit tests

### Phase 3 - Triage Categorization (Done)

- [x] `src/dss/triage.py`
- [x] `HT_05_triage_analysis.ipynb` (distribution, crosstab, threshold sensitivity)
- [x] Unit tests (boundary coverage)

### Phase 4 - Visualization (Done)

- [x] `src/visualization/plots.py` - distribution, correlation, boxplot, scatter, histogram, radar
- [x] `scripts/make_figures.py` + `HT_06_visualization.ipynb`
- [x] All figures generated in `outputs/figures/`

### Phase 5 - Local Pipeline (Done)

- [x] `scripts/run_pipeline.py`, `run_triage.py`, `generate_report.py`, `make_figures.py`
- [x] HTML report template (`templates/report.html`)
- [x] Streamlit dashboard (`app.py`, optional)

### Phase 6 - Colab Notebook (Done)

- [x] Self-contained `colab/HeartTriage_DSS_Colab.ipynb` (upload-based, no repo clone)
- [x] Verified: all cells execute and charts render inline in the notebook

### Phase 8 - Testing (Done)

- [x] 29 tests passing (loader, cleaner, transformer, SAW, triage, config, helpers, E2E)
- [x] Lint clean: `black`, `isort`, `flake8` (CI-enforced via `.github/workflows/ci.yml`)

### Phase 9 - Release (Done)

- [x] Repository pushed: `main` + `develop` branches
- [x] CHANGELOG finalized and moved from Unreleased to 1.0.0
- [x] Tag `v1.0.0` created and pushed
- [x] GitHub Release published with full notes

---

## Post-Release Ideas (v1.x / v2.0)

- [ ] Threshold recalibration tooling (ROC-style analysis against the `class` label)
- [ ] Interactive weight-tuning mode in the Streamlit dashboard
- [ ] REST API (FastAPI) for scoring single patients
- [ ] Alternative MADM methods for comparison (WP, TOPSIS)
- [ ] Docker image for reproducible deployment
- [ ] Additional dataset validation (other UCI heart disease sites)

---

*Related: [CONTRIBUTING.md](../CONTRIBUTING.md) | [CHANGELOG.md](../CHANGELOG.md) | [Releases](https://github.com/bugkey24/hearttriage-dss/releases)*
