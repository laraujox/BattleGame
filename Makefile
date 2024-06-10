# Variables
SOURCE := source
TESTS := tests
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
FLASK = $(VENV)/bin/flask
PYTHON_FILES := ${SOURCE} ${TESTS} migrations

# Phony targets (not real files)
.PHONY: help create_venv install run test-unit db-upgrade db-new- run-test-db test-int clean

# Default target
help:
	@echo "Usage:"
	@echo "  make create_venv      - Create a virtual environment"
	@echo "  make install          - Install dependencies"
	@echo "  make run              - Run the Flask application and the local database"
	@echo "  make test-unit        - Run Unit tests"
	@echo "  make db-upgrade       - Execute database migrations"
	@echo "  make db-new-migration - Generate new migration from model change"
	@echo "  make run-test-db      - Run local database for integration tests"
	@echo "  make test-int         - Run Integration tests"
	@echo "  make clean            - Clean up the project"
	@echo "  make format           - Format all python files"
	@echo "  make coverage         - Displays the project test coverage"


# Create virtual environment
create_venv:
	python3 -m venv $(VENV)

# Install dependencies
install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install autoflake
	$(PIP) install black
	pre-commit install --hook-type pre-commit --hook-type pre-push

# Run the Flask application
run:
	docker-compose up db test_db -d
	#$(FLASK) run

# Execute database migrations
db-upgrade:
	$(FLASK) db upgrade

# Generate new migration from model change
db-new-migration:
	$(FLASK) db migrate -m "$(msg)"

# Run Unit Tests
test-unit:
	pytest tests/unit -vv --disable-warnings

# Run Integration Tests Mock Database
run-test-db:
	docker compose up test_db -d

# Run Integration Tests
test-int:
	pytest tests/integration -vv --disable-warnings

# Clean up the project
clean:
	docker-compose down -v --remove-orphans
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Format all python files with autoflake, isort and black
format:
	autoflake --remove-all-unused-imports -r ${PYTHON_FILES} -i
	black ${PYTHON_FILES}

# Displays the project test coverage
coverage:
	pytest --cov=${SOURCE} ${TESTS}
