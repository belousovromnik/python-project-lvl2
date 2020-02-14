install:
	@poetry install

test:
	poetry run pytest gendiff tests

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

run:
	poetry run gendiff before.json after.json

runa:
	poetry run gendiff /home/belrom/python-project-lvl2/before.json /home/belrom/python-project-lvl2/after.json

.PHONY: install test lint selfcheck check build
