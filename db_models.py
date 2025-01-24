from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db_client import Base

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
