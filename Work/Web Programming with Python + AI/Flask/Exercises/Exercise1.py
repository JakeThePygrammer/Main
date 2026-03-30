from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/hello")
def hello():
    return "Hello user!"

@app.route("/jakov")
def jakov():
    return "Jakov, hello! This is a test."

app.run(debug=True)