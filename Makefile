.PHONY: all clean test checks pc update docs

install:
	pre-commit install
	poetry install --sync

update:
	poetry up --latest

checks: pc install lint test

pc:
	pre-commit run -a

lint:
	poetry run poe lint

test:
	poetry run pytest -m 'not dbonline'

test-integration:
	docker compose -f docker-compose.test.yml up -d
	poetry run pytest
	docker compose -f docker-compose.test.yml down

docs:
	poetry run mkdocs serve
