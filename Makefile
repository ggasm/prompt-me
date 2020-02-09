SHELL = /bin/bash


setup-venv:
	python3.8 -m venv python-venv
	source python-venv/bin/activate

build:
	make pke
	make setup-requirements

pke:
	pip install git+https://github.com/boudinfl/pke.git
	python3.8 -m nltk.downloader stopwords
	python3.8 -m nltk.downloader universal_tagset
	python3.8 -m spacy download en

setup-requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	export FLASK_ENV=development && python3.8 run.py


clean:
	rm -rf python-venv
