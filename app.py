from flask import Flask, jsonify
from flask_socketio import SocketIO


import random
from extract import KeywordExtractor
from newsapi import NewsApi
from resource import Resource
from suggestion import Suggestion
from wikipedia import Wikipedia
from typing import List


resources = [Wikipedia(), NewsApi()]

APP_NAME = "prompt-me"
MAX_NUM_KEYWORDS = 10

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def homepage():
    return f"You have reached the homepage of {APP_NAME}"


example_keyword = "MyKeywordExample"
example_text = "Hello, my name is John Smith"

extractor = KeywordExtractor()


@app.route("/keyword_analysis_test")
def keyword_test():
    return jsonify(keyword_analysis(example_keyword))


@app.route("/text_analysis_test")
def text_test():
    return jsonify(text_analysis(example_text))


def text_analysis(paragraphs: List[str]) -> {str: List[Suggestion]}:
    text = "".join(paragraphs)
    keywords = extractor.extract_hot_keywords(text, MAX_NUM_KEYWORDS)
    random.shuffle(keywords)

    return {str(resource): [resource.lookup(keyword) for keyword in keywords] for resource in resources}


@socketio.on("paragraphs_from_client", namespace="/analyse")
def analyse(paragraphs):
    print(paragraphs)


# TESTING ONLY
def keyword_analysis(keyword: str) -> {Resource: List[Suggestion]}:
    return {str(resource): resource.lookup(example_keyword) for resource in resources}


print(NewsApi().lookup("Trump"))
# print(keyword_analysis(example_keyword))
