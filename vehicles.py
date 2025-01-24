import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand
        self.model = model

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            logging.error(f"Unexpected type! Expected type str, got {type(brand)}")

    def display_info(self):
        print(f"Brand is a {self._brand}. Model is a {self.__model}.")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super.__init__(self, brand, model)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Brand is a {self.brand}. Model is a {self.model}. Doors number is {self.num_doors}.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super.__init__(self, brand, model)
        self.has_sidecar = has_sidecar

    def display_info(self):
        print(f"Brand is a {self.brand}. Model is a {self.model}. Sidecar is {self.has_sidecar}.")
