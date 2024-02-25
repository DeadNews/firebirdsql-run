.PHONY: all clean test checks

install-all: install pc-install

install:
	poetry install --sync

pc-install:
	pre-commit install

update-latest:
	poetry up --latest

checks: pc-run install lint test

pc-run:
	pre-commit run -a

lint:
	poetry run poe lint

test:
	poetry run pytest -m 'not dbonline'

test-integration:
	docker compose -f docker-compose.test.yml up -d
	poetry run pytest
	docker compose -f docker-compose.test.yml down

docs-serve:
	poetry run mkdocs serve
