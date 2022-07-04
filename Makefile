setup:
	python3 -m venv ~/.myrepo434

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=myrepo434lib tests/*.py


lint:
	pylint --disable=R,C myrepo434lib

all: install lint test
