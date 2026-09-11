# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Interactive P1 radar chart profile in `make_figures` and `HT_06` notebook

## [1.0.0] - 2026-09-11

Initial public release: complete Decision Support System for cardiac ER triage.

### Added

- **Core package (`src/`)**
  - `config.py` — centralized criteria, SAW weights (sum = 1.0), triage thresholds, and categorical mappings
  - `data/loader.py` — whitespace-delimited parser for `cleve.mod` (comment-header aware)
  - `data/cleaner.py` — `?` missing-marker handling, numeric coercion, duplicate removal (303 → 296 records)
  - `data/transformer.py` — symbolic-to-ordinal mapping for 7 clinical attributes
  - `dss/saw.py` — benefit/cost normalization (zero-division safe) and weighted scoring
  - `dss/triage.py` — P1/P2/P3 categorization with configurable thresholds
  - `visualization/plots.py` — triage distribution, correlation heatmap, boxplot, scatter, score histogram with thresholds, interactive P1 radar chart
  - `utils/logger.py` (rich console) and `utils/helpers.py` (distribution tables)
- **Scripts** — `run_pipeline.py` (full pipeline), `run_triage.py` (summary), `generate_report.py` (Jinja2 HTML report), `make_figures.py` (all standard figures)
- **Notebooks** — `HT_01`–`HT_06` (understanding, cleaning, transformation, SAW with manual walkthrough, triage analysis with threshold sensitivity, visualization)
- **`colab/HeartTriage_DSS_Colab.ipynb`** — self-contained Colab edition; no repo clone needed, all charts render inline
- **HTML report template** (`templates/report.html`) with triage distribution, actions, and sample results
- **Streamlit dashboard** (`app.py`) — CSS-optional, filters by triage level and age range, CSV export (requires `pip install .[dashboard]`)
- **Quality tooling**
  - 29 unit/integration tests (loader, cleaner, transformer, SAW, triage, config invariants, helpers, end-to-end on the real dataset)
  - `pyproject.toml` packaging, `.flake8`, black + isort configuration
  - GitHub Actions CI: lint, format checks, and tests across Python 3.10–3.12
  - Makefile targets (`install`, `run`, `figures`, `test`, `format`, `lint`, `clean`)
- **Documentation**
  - README with project overview, data description, and embedded result figures
  - Modular `docs/`: index, architecture, methodology, data dictionary, pipeline, user guide, roadmap, glossary, references
  - Documentation templates (doc, module, notebook, ADR) in `docs/templates/`
  - CHANGELOG, CONTRIBUTING (Git Flow + Conventional Commits), CODE_OF_CONDUCT, MIT LICENSE

### Fixed

- `thal` criterion mapping: dataset token is `fix`, not the canonical `fixed` — 18 rows previously resolved to NaN
- Cost normalization zero-division when a criterion minimum is 0 (e.g. `ca` = 0)

### Metric Snapshot (v1.0.0)

| Triage | Category | Count | Percentage |
|--------|----------|------:|-----------:|
| P1 | Emergency | 126 | 42.6% |
| P2 | Urgent | 116 | 39.2% |
| P3 | Non-Urgent | 54 | 18.2% |

[Unreleased]: https://github.com/bugkey24/hearttriage-dss/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/bugkey24/hearttriage-dss/releases/tag/v1.0.0
