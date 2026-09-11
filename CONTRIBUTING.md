# Contributing to HeartTriage DSS

First off, thank you for considering contributing! 

Following these guidelines helps communicate that you respect the time of
developers managing this project. In return, they should reciprocate that
respect by addressing your issue, assessing changes, and helping you finalize
your pull requests.

---

## Table of Contents

1. [Code of Conduct](#-code-of-conduct)
2. [Getting Started](#-getting-started)
3. [How Can I Contribute?](#-how-can-i-contribute)
4. [Git Workflow](#-git-workflow)
5. [Commit Convention](#-commit-convention)
6. [Coding Standards](#-coding-standards)
7. [Testing](#-testing)
8. [Documentation](#-documentation)
9. [Pull Request Process](#-pull-request-process)

---

## Code of Conduct

This project adheres to the [Contributor Covenant](CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code.

---

## Getting Started

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone https://github.com/bugkey24/hearttriage-dss.git
cd hearttriage-dss

# 2. Add upstream remote
git remote add upstream https://github.com/bugkey24/hearttriage-dss.git

# 3. Create virtual environment
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the test suite to verify setup
pytest tests/ -v
```

---

## How Can I Contribute?

### Reporting Bugs

- Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- Include: dataset sample (if relevant), expected vs actual behavior, environment info
- Check existing issues first to avoid duplicates

### Suggesting Enhancements

- Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- Explain the clinical/DSS rationale — e.g., recalibrated weights, new criteria
- Reference the [methodology docs](docs/methodology.md) where applicable

### Good First Issues

- Documentation improvements
- Additional unit tests
- New visualizations in `src/visualization/`

---

## Git Workflow

We use a **simplified Git Flow**:

```
main (production)
  │
  ├── develop (integration)
  │     ├── feature/<name>    ← new features
  │     └── ...
  │
  └── hotfix/<name>           ← urgent fixes to main
```

```bash
# 1. Sync with upstream
git checkout develop && git pull upstream develop

# 2. Create a feature branch
git checkout -b feature/saw-engine

# 3. Commit changes (see convention below)

# 4. Push & open a Pull Request to develop
git push origin feature/saw-engine
```

| Branch type | Prefix       | Merges into |
|-------------|--------------|-------------|
| Production  | `main`       | —           |
| Integration | `develop`    | `main`      |
| Feature     | `feature/`   | `develop`   |
| Hotfix      | `hotfix/`    | `main`      |
| Release     | `release/`   | `main` + `develop` |

---

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

| Type       | Function        | Example                                                   |
|------------|-----------------|-----------------------------------------------------------|
| `feat`     | New feature     | `feat(loader): add whitespace delimiter parser`           |
| `fix`      | Bug fix         | `fix(cleaner): handle '?' as missing value`               |
| `docs`     | Documentation   | `docs(readme): add installation guide`                    |
| `style`    | Formatting      | `style(saw): format with black`                           |
| `refactor` | Refactoring     | `refactor(triage): extract threshold config`              |
| `test`     | Testing         | `test(saw): add unit test for normalization`              |
| `chore`    | Maintenance     | `chore(deps): bump pandas to 2.2`                         |
| `data`     | Data changes    | `data(raw): add cleve.mod dataset`                        |

> Done Keep subjects ≤ 72 chars, imperative mood ("add", not "added").

---

## Coding Standards

| Tool      | Purpose         | Command                          |
|-----------|-----------------|----------------------------------|
| `black`   | Formatter       | `black src/ scripts/ tests/`     |
| `isort`   | Import sorting  | `isort src/ scripts/ tests/`     |
| `flake8`  | Linter          | `flake8 src/ scripts/ tests/`    |
| `mypy`    | Type checking   | `mypy src/`                      |

- Follow **PEP 8**; use `snake_case` for modules/functions, `PascalCase` for classes
- Add **type hints** to all public functions
- Docstrings: Google style — see existing modules in `src/`
- Configuration (weights, thresholds, mappings) lives in `src/config.py` — never hard-code

---

## Testing

```bash
pytest tests/ -v
```

- Every new function in `src/` needs a corresponding test in `tests/`
- Tests must pass before a PR can be merged
- Use small synthetic DataFrames for edge cases (missing `?`, empty rows)

---

## Documentation

- All docs live in `docs/` — split by topic, never one giant file
- Use the templates in [`docs/templates/`](docs/templates/) for new pages
- Update [`CHANGELOG.md`](CHANGELOG.md) under **[Unreleased]** for user-facing changes
- Update [`docs/roadmap.md`](docs/roadmap.md) status tables when milestones complete

---

## Pull Request Process

1. Ensure `pytest`, `black`, and `flake8` pass locally
2. Update documentation & changelog for any behavior change
3. Fill out the PR template completely
4. Request review from a maintainer
5. Squash-merge into `develop` with a conventional commit title

>  Releases are tagged `vX.Y.Z` (SemVer) from `main` with an updated changelog.

---

<div align="center">

_Thank you for contributing! _

</div>
