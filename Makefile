SHELL = /bin/bash

setup:
	python3 -m venv python-venv
	pip3 install -r requirements.txt

run:
	source python-venv/bin/activate
	export FLASK_ENV=development && python3 run.py	

clean:
	rm -rf python-venv
