from create_tables import Product, User, Brand, Category, SessionLocal

session = SessionLocal()


def get_all_products():
    return session.query(Product).all()

def get_one_product(id):
    return session.query(Product).filter(Product.id == id).one()

def get_all_users():
    return session.query(User).all()

def get_one_user(id):
    return session.query(User).filter(User.id == id).one()

def get_all_brands():
    return session.query(Brand).all()

def get_one_brand(id):
    return session.query(Brand).filter(Brand.id == id).one()

def get_all_categories():
    return session.query(Category).all()

def get_one_category(id):
    return session.query(Category).filter(Category.id == id).one()