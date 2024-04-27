class Hero:
    def __init__(self, name, health=100, attack_power=20):
        """Конструктор класса Hero.

        Параметры:
        name (str): Имя героя.
        health (int, optional): Начальное значение здоровья героя. По умолчанию равно 100.
        attack_power (int, optional): Сила атаки героя. По умолчанию равна 20.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атакует другого героя, уменьшая его здоровье.

        Параметры:
        other (Hero): Герой, который подвергается атаке.
        """
        other.health -= self.attack_power
        if other.health < 0:  # Убедимся, что здоровье не уходит в отрицательное значение
            other.health = 0

    def is_alive(self):
        """Проверяет, жив ли герой.

        Возвращает:
        bool: True, если здоровье героя больше 0, иначе False.
        """
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name):
        """Инициализирует игру с двумя героями: игроком и компьютером."""
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """Запускает игровой процесс, чередуя ходы игрока и компьютера."""
        turn = 0  # Счётчик ходов для определения, кто атакует
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:  # Ход игрока
                attacker, defender = self.player, self.computer
            else:  # Ход компьютера
                attacker, defender = self.computer, self.player

            attacker.attack(defender)
            print(f"{attacker.name} атакует {defender.name}, у {defender.name} осталось {defender.health} здоровья.")

            if not defender.is_alive():
                break  # Если защитник побеждён, выходим из цикла

            turn += 1  # Переключаем ход

        winner = self.player if self.player.is_alive() else self.computer
        print(f"Игра окончена. Победитель: {winner.name}")
