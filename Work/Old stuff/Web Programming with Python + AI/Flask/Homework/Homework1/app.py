from flask import Flask, render_template
from queries import get_all_cities, get_one_city

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cities")
def products():
    cities = get_all_cities()
    return render_template("cities.html", cities=cities)

@app.route("/city/<int:id>")
def product(id):
    city = get_one_city(id)
    return render_template("city_details.html", city=city)

app.run()