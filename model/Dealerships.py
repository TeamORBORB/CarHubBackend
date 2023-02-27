from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dealership(Base):
    __tablename__ = 'dealership'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

engine = create_engine('sqlite:///dealerships.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example data
dealership1 = Dealership(name='Bobs Auto', address='123 Main St', latitude=37.7749, longitude=-122.4194)
dealership2 = Dealership(name='Janes Cars', address='456 Market St', latitude=37.7911, longitude=-122.3963)

session.add(dealership1)
session.add(dealership2)
session.commit()
