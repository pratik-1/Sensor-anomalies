install:
	pip install --upgrade pip &&\
        pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test:
	pytest -v --cov-report term-missing --cov=. anomalies/tests/test_count_anomalies.py

all: install format lint test