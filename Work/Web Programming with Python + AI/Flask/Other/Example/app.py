from flask import Flask, render_template
from queries import get_all_products, get_one_product, get_all_users

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/products")
def products():
    products = get_all_products()
    return render_template("products.html", products=products)

@app.route("/products/<int:id>")
def product(id):
    product = get_one_product(id)
    # 1. prochitaj produkt so id = id od baza

    # 2. renderiraj template so site podatoci za ovoj produkt (id, name, price, category, brand)

    return render_template("product.html", product=product)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name.title())

app.run(debug=True)