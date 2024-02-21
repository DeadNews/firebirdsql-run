.PHONY: all clean test checks

install-all: install pc-install

install:
	poetry install --sync

pc-install:
	pre-commit install

update-latest:
	poetry up --latest

checks: pc-run install lint pyright test

pc-run:
	pre-commit run -a

lint:
	poetry run poe lint

pyright:
	poetry run poe pyright

test:
	poetry run pytest -m 'not dbonline'

test-integration:
	docker compose -f docker-compose.test.yml up -d
	poetry run pytest
	docker compose -f docker-compose.test.yml down
