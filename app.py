from flask import Flask
from flask_socketio import SocketIO

from newsapi import NewsApi
from wikipedia import Wikipedia

resources = [Wikipedia(), NewsApi()]

APP_NAME = "prompt-me"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def homepage():
    return f"You have reached the homepage of {APP_NAME}"


def test_resources():

    for resource in resources:
        resource.lookup("MyKeywordExample")


test_resources()
