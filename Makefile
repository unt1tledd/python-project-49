install:
	poetry install
brain-games:
	poetry run python brain_game.py
lint:
	poetry run flake8 brain_game.py
brain-even:
	poetry run python brain_even.py
brain-calc:
	poetry run python brain_calc.py
brain-gcd:
	poetry run python brain_gcd.py
brain-progression:
	poetry run python brain_progression.py
brain-prime:
	poetry run python brain_prime.py
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl