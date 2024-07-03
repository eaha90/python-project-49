install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

make lint:
	poetry run flake8 brain_games

make lint:
	poetry run flake8 brain_games
