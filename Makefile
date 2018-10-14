install:
	pip install -r requirements.txt;

test:
	pytest --cov=main ./tests;

run:
	python app.py
