from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/thi")
def thi():
    return "Welcome to TIIDE World"
