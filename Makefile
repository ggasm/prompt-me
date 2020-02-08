SHELL = /bin/bash

run:
	source python-venv/bin/activate
	export FLASK_ENV=development
	python run.py
