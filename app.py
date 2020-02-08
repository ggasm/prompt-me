from flask import Flask, render_template
from flask_socketio import SocketIO

APP_NAME = "prompt-me"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def homepage():
    return f"You have reached the homepage of {APP_NAME}"