.PHONY: help install clean test build run-example

PYTHON=python
VENV=.venv
ACTIVATE=. $(VENV)/bin/activate;

help:
	@echo "Available commands:"
	@echo "  make install       Set up virtual environment and install dependencies"
	@echo "  make run-example   Run a sample preset policy and generate JSON"
	@echo "  make test          Run unit tests with pytest"
	@echo "  make build         Build project for CLI usage"
	@echo "  make clean         Remove cache and venv"

install:
	@test -d $(VENV) || python -m venv $(VENV)
	@$(ACTIVATE) pip install -r requirements.txt
	@echo "✅ Environment ready."

run-example:
	@$(ACTIVATE) $(PYTHON) -m iam_policy_generator.cli generate \
		--preset s3:read-only \
		--resources arn:aws:s3:::example-bucket/* \
		--output examples/sample_output.json

test:
	@$(ACTIVATE) pytest tests/

build:
	@$(ACTIVATE) pip install build
	@$(ACTIVATE) python -m build

clean:
	rm -rf $(VENV) dist *.egg-info __pycache__ .pytest_cache .mypy_cache
	find . -type d -name "__pycache__" -exec rm -r {} +
