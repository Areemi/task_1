from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# БД
DATABASE_URL = "sqlite:///vehicles.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


# Модели
class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)


class Car(Vehicle):
    __tablename__ = 'cars'

    id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    num_doors = Column(Integer, nullable=False)


class Motorcycle(Vehicle):
    __tablename__ = 'motorcycles'

    id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    has_sidecar = Column(Boolean, default=False)


# Методы для работы с базой данных
def add_vehicle(vehicle):
    session = Session()
    session.add(vehicle)
    session.commit()
    session.close()

def update_vehicle(vehicle_id, brand=None, model=None, **kwargs):
    session = Session()
    vehicle = session.query(Vehicle).get(vehicle_id)
    if vehicle:
        if brand:
            vehicle.brand = brand
        if model:
            vehicle.model = model
        for key, value in kwargs.items():
            setattr(vehicle, key, value)
        session.commit()
    session.close()

def delete_vehicle(vehicle_id):
    session = Session()
    vehicle = session.query(Vehicle).get(vehicle_id)
    if vehicle:
        session.delete(vehicle)
        session.commit()
    session.close()