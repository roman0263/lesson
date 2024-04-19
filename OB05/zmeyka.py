import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна игры
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

# Установка заголовка окна
pygame.display.set_caption("Змейка")

class Snake:
    def __init__(self):
        self.body = [(20, 20), (20, 21), (20, 22)]  # Начальное положение змейки
        self.direction = (0, -1)  # Начальное направление движения (вверх)
        self.grow = False  # Нужно ли змейке расти

    def move(self):
        if not self.grow:
            self.body.pop(0)  # Удаление последнего элемента, если змейка не растет
        self.grow = False  # Сброс флага роста

        head_x, head_y = self.body[-1]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)  # Вычисление новой головы
        self.body.append(new_head)  # Добавление новой головы в список тела

    def change_direction(self, new_direction):
        # Изменение направления, если это не приводит к движению назад
        if (new_direction[0] * self.direction[0] == 0 and
            new_direction[1] * self.direction[1] == 0):
            self.direction = new_direction

    def check_collision(self):
        head = self.body[-1]
        return head in self.body[:-1]  # Проверка столкновения головы с телом

    def grow_up(self):
        self.grow = True  # Установка флага роста, чтобы змейка выросла после следующего движения


import random

class Food:
    def __init__(self, window_width, window_height, cell_size):
        self.window_width = window_width
        self.window_height = window_height
        self.cell_size = cell_size
        self.position = self.spawn_food()

    def spawn_food(self):
        # Генерация случайной позиции для еды
        x = random.randint(0, (self.window_width - self.cell_size) // self.cell_size) * self.cell_size
        y = random.randint(0, (self.window_height - self.cell_size) // self.cell_size) * self.cell_size
        return (x, y)

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake()
        self.food = Food(800, 600, 20)  # Примерные значения для размеров окна и размера ячейки

    def run(self):
        running = True
        while running:
            # Основной цикл игры будет реализован здесь
            pass


# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Здесь будет обновление игры

    # Здесь будет отрисовка элементов игры

    # Обновление содержимого экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
sys.exit()


