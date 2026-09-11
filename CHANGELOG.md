# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project structure (`data/`, `src/`, `scripts/`, `notebooks/`, `tests/`, `docs/`, `colab/`, `outputs/`)
- Modular documentation split from `PROJECT.md` into `docs/`
- Documentation templates in `docs/templates/`
- Project logo & badges (`assets/images/logo.svg`)
- README with quick start, usage, and documentation index
- CONTRIBUTING guidelines, Code of Conduct, issue & PR templates
- `requirements.txt`, `environment.yml`, `.gitignore`, `Makefile`, `pyproject.toml`, `.flake8`
- CI workflow (`.github/workflows/ci.yml`)
- Analysis notebooks `HT_01` … `HT_06` (understanding, cleaning, transformation, SAW, triage, visualization)
- `scripts/make_figures.py` — renders all standard figures incl. interactive P1 radar chart
- Streamlit dashboard `app.py` (optional, `pip install .[dashboard]`)
- Test suite: 29 unit + integration tests (loader, cleaner, transformer, SAW, triage, config, helpers, E2E)

### Fixed

- `thal` mapping: dataset token is `fix` (not `fixed`); 18 rows previously unmapped → NaN
- Cost normalization zero-division when a criterion's minimum is 0 (e.g. `ca`)

### Changed

- Renamed project terminology from SPK to **DSS** consistently across all documents

## [1.0.0] - TBA

- Initial public release

[Unreleased]: https://github.com/bugkey24/hearttriage-dss/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/bugkey24/hearttriage-dss/releases/tag/v1.0.0
