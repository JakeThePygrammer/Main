from create_tables import Product, User, SessionLocal

session = SessionLocal()


def get_all_products():
    return session.query(Product).all()

def get_one_product(id):
    return session.query(Product).filter(Product.id == id).one()

def get_all_users():
    return session.query(User).all()