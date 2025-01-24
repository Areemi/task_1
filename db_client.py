from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from db_models import Vehicle

Base = declarative_base()


# БД
DATABASE_URL = "sqlite:///vehicles.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)



# Методы для работы с базой данных
class DbClient:
    Session = sessionmaker(bind=engine)

    @staticmethod
    def add_vehicle(vehicle):
        """Добавляет новое транспортное средство"""
        with DbClient.Session.begin() as session:
            session.add(vehicle)

    @staticmethod
    def update_vehicle(vehicle_id, brand=None, model=None, **kwargs):
        """Обновляет данные транспортного средство по id"""
        with DbClient.Session.begin() as session:
            vehicle = session.query(Vehicle).get(vehicle_id)
            if vehicle:
                if brand:
                    vehicle.brand = brand
                if model:
                    vehicle.model = model
                for key, value in kwargs.items():
                    setattr(vehicle, key, value)

    @staticmethod
    def delete_vehicle(vehicle_id):
        """Удаляет транспортное средство по id"""
        with DbClient.Session.begin() as session:
            vehicle = session.query(Vehicle).get(vehicle_id)
            if vehicle:
                session.delete(vehicle)
