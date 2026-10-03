from create_tables import City, SessionLocal

session = SessionLocal()


def get_all_cities():
    return session.query(City).all()

def get_one_city(id):
    return session.query(City).filter(City.id == id).one()
