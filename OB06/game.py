# main.py

# Импорт классов
from hero import Hero
from game import Game


def main():
    # Создание героев и игры
    player_name = input("Введите имя игрока: ")
    computer_name = "Компьютерный Противник"

    # Инициализация игры
    game = Game(player_name, computer_name)

    # Начало игры
    game.start()


if __name__ == "__main__":
    main()
