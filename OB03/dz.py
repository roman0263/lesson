# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        return f"{self.name} издает звук"

    def eat(self):
        return f"{self.name} ест"

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} поет"

    def get_species(self):
        return "Птица"

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} рычит"

    def get_species(self):
        return "Млекопитающее"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} шипит"

    def get_species(self):
        return "Рептилия"

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)

    def list_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}, Вид: {animal.get_species()}")

    def list_staff(self):
        for person in self.staff:
            print(f"Сотрудник: {person.get_role()}")

class ZooKeeper:
    def feed_animal(self, animal):
        return f"{animal.name} был накормлен"

    def get_role(self):
        return "Смотритель"

class Veterinarian:
    def heal_animal(self, animal):
        return f"{animal.name} был вылечен"

    def get_role(self):
        return "Ветеринар"

def save_zoo(zoo, filename):
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)

def load_zoo(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

zoo = Zoo()

parrot = Bird("Вася", 3)
tiger = Mammal("Шах", 5)
snake = Reptile("Горыныч", 4)

zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(snake)

keeper = ZooKeeper()
vet = Veterinarian()

zoo.add_staff(keeper)
zoo.add_staff(vet)

zoo.list_animals()
zoo.list_staff()

# Сохранение текущего состояния зоопарка
save_zoo(zoo, 'zoo_state.pickle')

# Загрузка сохранённого состояния зоопарка
loaded_zoo = load_zoo('zoo_state.pickle')

# Проверка загруженных данных
loaded_zoo.list_animals()
loaded_zoo.list_staff()
