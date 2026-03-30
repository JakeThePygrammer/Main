from flask import Flask, render_template
from queries import get_all_products, get_one_product, get_all_users, get_one_user,get_all_categories,get_one_category,get_all_brands,get_one_brand

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

@app.route("/users")
def users():
    users = get_all_users()
    return render_template("users.html", users=users)

@app.route("/userbyid/<id>")
def userid(id):
    user = get_one_user(id)
    return render_template("userbyid.html", user=user)

@app.route("/categories")
def categories():
    categories = get_all_categories()
    return render_template("categories.html", categories=categories)

@app.route("/brands")
def brands():
    brands = get_all_brands()
    return render_template("brands.html", brands=brands)

@app.route("/category/<id>")
def category(id):
    category = get_one_category(id)
    return render_template("category.html", category=category)

@app.route("/brand/<id>")
def brand(id):
    brand = get_one_brand(id)
    return render_template("brand.html", brand=brand)

app.run(debug=True)

