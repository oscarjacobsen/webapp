from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World mafa!</p>"

@app.route("/test")
def test():
    return "<p>Testing this amazing new route tjommi!</p>"