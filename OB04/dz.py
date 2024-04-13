from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"



class Fighter():
    def __init__(self, weapon : Weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon : Weapon):
        self.weapon = new_weapon

    def attack(self):
        return self.weapon.attack()

class Monster:
    def defend(self, action):
        if "лука" in action:
            return "Монстр ранен"
        elif "мечом" in action:
            return "Монстр побежден!"


def main():
    sword = Sword()
    bow = Bow()
    monster = Monster()

    fighter = Fighter(bow)  # Боец начинает с лука
    print("Боец выбирает лук.")
    action = fighter.attack()
    print(action)
    print(monster.defend(action))

    fighter.change_weapon(sword)  # Боец меняет оружие на меч
    print("\nБоец выбирает меч.")
    action = fighter.attack()
    print(action)
    print(monster.defend(action))

if __name__ == "__main__":
    main()


