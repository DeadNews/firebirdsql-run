.PHONY: all clean default install lock update checks pc test docs run

default: checks

install:
	pre-commit install
	poetry install --sync

lock:
	poetry lock --no-update

update:
	poetry up --latest

checks: pc install lint test

pc:
	pre-commit run -a

lint:
	poetry run poe lint

test:
	poetry run pytest -m 'not dbonline'

docs:
	poetry run mkdocs serve

test-integration:
	docker compose -f docker-compose.test.yml up -d
	poetry run pytest
	docker compose -f docker-compose.test.yml down

bumped:
	git cliff --bumped-version

# make release-tag_name
# make release-$(git cliff --bumped-version)-alpha.0
release-%: checks
	git cliff -o CHANGELOG.md --tag $*
	pre-commit run --files CHANGELOG.md || pre-commit run --files CHANGELOG.md
	git add CHANGELOG.md
	git commit -m "chore(release): prepare for $*"
	git push
	git tag -a $* -m "chore(release): $*"
	git push origin $*
	git tag --verify $*
