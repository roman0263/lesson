import unittest
from DZ_game import Hero
from DZ_game import Game
class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero1 = Hero("Герой1")
        self.hero2 = Hero("Герой2")

    def test_attack(self):
        """Проверка функциональности атаки."""
        self.hero1.attack(self.hero2)
        self.assertEqual(self.hero2.health, 80)  # Предполагаем, что attack_power = 20

    def test_is_alive(self):
        """Проверка, что герой жив или мёртв в зависимости от здоровья."""
        self.assertTrue(self.hero1.is_alive())
        self.hero1.health = 0
        self.assertFalse(self.hero1.is_alive())

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("Игрок", "Компьютер")

    def test_game_end(self):
        """Проверка, что игра заканчивается, когда здоровье одного из героев падает до 0."""
        self.game.player.health = 20
        self.game.computer.health = 20
        self.game.start()
        self.assertTrue(not self.game.player.is_alive() or not self.game.computer.is_alive())

if __name__ == '__main__':
    unittest.main()
