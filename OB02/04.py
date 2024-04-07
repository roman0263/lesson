class Car():
    def __init__(self, make, model):
        self.public_make = make
        self._protected_model = model
        self.__private_year = 2022

    def public_metod(self):
        return f"Это публичный метод. Машина: {self.public_make} {self._protected_model}"
    def protected_metod(self):
        return "Это защищенный метод "
    def private_matod(self):
        return "Это приватный метод"


class ElectricCar(Car):
    def __init__(self, make, model,battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        details = f"{self.public_make} {self._protected_model} Батарея: {self.battery_size} kwh"
        return details

tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.public_make)
print(tesla.public_metod())
print(tesla._protected_model)
print(tesla.protected_metod())
print(tesla._Car__private_year)