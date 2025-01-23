

class Vehicle:
    """Vehicle"""
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand
        else:
            print("Unexpected type")
    

    def display_info(self):
        print(f"Brand is a {self.__brand}. Model is a {self.__model}.")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        Vehicle.__init__(self, brand, model)
        self.num_doors = num_doors

    def display_info(self):
        super().__init__()
        print(f"Brand is a {self.brand}. Model is a {self.model}. Doors number is {self.num_doors}.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        Vehicle.__init__(self, brand, model)
        self.has_sidecar = has_sidecar

    def display_info(self):
        print(f"Brand is a {self.brand}. Model is a {self.model}. Sidecar is {self.has_sidecar}.")
