from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "This is the home page."

@app.route("/contact")
def contact():
    return "Contact me - 070 123 456"

@app.route("/about")
def about():
    return "About me - Hi! I'm Jakov. I'm 13 years old!"

app.run(debug=True)