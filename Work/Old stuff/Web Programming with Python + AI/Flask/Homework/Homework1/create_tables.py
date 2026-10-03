from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    characteristics = Column(String)
    population = Column(Integer)
    architecture = Column(String)


engine = create_engine("sqlite:///cities.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)