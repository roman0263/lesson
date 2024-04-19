import pygame
import random

# Инициализируем библиотеку Pygame
pygame.init()

# Определение размеров экрана и размера блока
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
FPS = 10  # Устанавливаем количество кадров в секунду

# Определяем цвета, используемые в игре
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)  # RGB для черного цвета
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (255, 0, 0),    # Red
    (128, 0, 128)   # Purple
]

# Определение форм тетромино
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

# Класс для управления фигурами
class Piece:
    def __init__(self, x, y):
        self.shape = random.choice(SHAPES)  # Выбор случайной формы
        self.color = random.choice(COLORS)  # Выбор случайного цвета
        self.x = x  # Начальное положение по горизонтали
        self.y = y  # Начальное положение по вертикали
        self.rotation = 0  # Состояние вращения

    def rotate(self):
        # Поворачиваем фигуру на 90 градусов
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        self.rotation = (self.rotation + 1) % 4

    def draw(self, screen):
        # Отрисовка фигуры на экране
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, (self.x + j * BLOCK_SIZE, self.y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

class Tetris:
    def __init__(self, width, height):
        self.width = width  # Ширина игрового поля в блоках
        self.height = height  # Высота игрового поля в блоках
        self.grid = [[0 for _ in range(width)] for _ in range(height)]  # Сетка игрового поля
        self.piece = Piece(width // 2 - 2, 0)  # Создаем новую фигуру

    def check_collision(self):
        # Проверяем столкновения с границами поля и другими фигурами
        for i, row in enumerate(self.piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    if (self.piece.y + i) >= self.height or \
                       (self.piece.x + j) < 0 or \
                       (self.piece.x + j) >= self.width or \
                       self.grid[self.piece.y + i][self.piece.x + j]:
                        return True
        return False

    def freeze_piece(self):
        # "Замораживаем" фигуру на месте и создаем новую
        for i, row in enumerate(self.piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.piece.y + i][self.piece.x + j] = self.piece.color
        self.piece = Piece(self.width // 2 - 2, 0)

    def move_piece(self, dx, dy):
        # Перемещаем фигуру
        old_x, old_y = self.piece.x, self.piece.y
        self.piece.x += dx
        self.piece.y += dy
        if self.check_collision():
            # Если произошло столкновение, возвращаем фигуру назад
            self.piece.x, self.piece.y = old_x, old_y
            if dy:
                self.freeze_piece()

    def draw_grid(self, screen):
        # Отрисовка сетки игрового поля
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                else:
                    pygame.draw.rect(screen, GRAY, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Настройка Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
game = Tetris(SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_piece(-1, 0)
            elif event.key == pygame.K_RIGHT:
                game.move_piece(1, 0)
            elif event.key is pygame.K_DOWN:
                game.move_piece(0, 1)
            elif event.key == pygame.K_UP:
                game.piece.rotate()
                if game.check_collision():
                    # Если после вращения произошло столкновение, возвращаем фигуру в исходное положение
                    game.piece.rotate()
                    game.piece.rotate()
                    game.piece.rotate()

    game.move_piece(0, 1)  # Автоматическое падение фигуры вниз каждый тик
    screen.fill(BLACK)  # Очищаем экран
    game.draw_grid(screen)  # Отрисовываем сетку
    game.piece.draw(screen)  # Отрисовываем текущую фигуру
    pygame.display.flip()  # Обновляем экран
    clock.tick(FPS)  # Контроль частоты кадров

pygame.quit()
