# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

import pickle
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        return f"{self.name}издает звук"

    def eat(self):
        return f"{self.name} ест"


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} поет"

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} рычит"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} шипит"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)
class ZooKeeper:
    def feed_animal(self, animal):
        return f"{animal.name} был накормлен"

class Veterinarian:
    def heal_animal(self, animal):
        return f"{animal.name} был вылечен"



def save_zoo(zoo, filename):
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)

def load_zoo(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
