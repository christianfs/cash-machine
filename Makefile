init:
	pip install -r requirements.txt;

test:
	pytest --cov=main ./tests;
