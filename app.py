from flask import Flask
from flask_socketio import SocketIO

from newsapi import NewsApi
from wikipedia import Wikipedia
#from books import BooksApi

resources = [Wikipedia(), NewsApi()]

APP_NAME = "prompt-me"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def homepage():
    return f"You have reached the homepage of {APP_NAME}"


example_keyword = "MyKeywordExample"


@app.route("/dummy_test")
def test_resources():
    return keyword_anlaysis(example_keyword)


def keyword_anlaysis(keyword):
    return {resource.get_name(): resource.lookup(example_keyword) for resource in resources}


print(keyword_anlaysis(example_keyword))
