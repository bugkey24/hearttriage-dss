.PHONY: install run triage report test format lint clean help

install:            ## Install dependencies
	pip install -r requirements.txt

run:                ## Run the full DSS pipeline
	python scripts/run_pipeline.py

triage:             ## Run triage scoring only
	python scripts/run_triage.py

report:             ## Generate HTML report
	python scripts/generate_report.py

test:               ## Run test suite
	pytest tests/ -v

format:             ## Format code (black + isort)
	black src/ scripts/ tests/
	isort src/ scripts/ tests/

lint:               ## Lint code
	flake8 src/ scripts/ tests/

clean:              ## Remove generated outputs
	rm -rf outputs/figures/* outputs/reports/* outputs/logs/*
	rm -rf data/interim/* data/processed/*
	find . -type d -name __pycache__ -exec rm -rf {} +

help:               ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'
