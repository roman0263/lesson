import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна игры
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

# Установка заголовка окна
pygame.display.set_caption("Змейка")

class Snake:
    def __init__(self):
        self.body = [(100, 100), (100, 120), (100, 140)]  # Изменено для предотвращения немедленного столкновения
        self.direction = (0, -20)  # Поправлено на большее расстояние
        self.grow = False

    def move(self):
        if not self.grow:
            self.body.pop(0)
        self.grow = False

        head_x, head_y = self.body[-1]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.append(new_head)

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def check_collision(self):
        head = self.body[-1]
        return head in self.body[:-1]

    def grow_up(self):
        self.grow = True

class Food:
    def __init__(self, window_width, window_height, cell_size):
        self.window_width = window_width
        self.window_height = window_height
        self.cell_size = cell_size
        self.position = self.spawn_food()

    def spawn_food(self):
        while True:
            x = random.randint(0, (self.window_width - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.window_height - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake.body:
                return (x, y)

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake()
        self.food = Food(window_width, window_height, 20)
        self.food.snake = self.snake  # Pass snake reference to food for collision checking
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -20))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 20))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-20, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((20, 0))

            self.snake.move()
            if self.snake.body[-1] == self.food.position:
                self.snake.grow_up()
                self.food.position = self.food.spawn_food()

            self.window.fill((0, 0, 0))
            self.draw_objects()
            pygame.display.flip()
            self.clock.tick(10)

    def draw_objects(self):
        for segment in self.snake.body:
            pygame.draw.rect(self.window, (0, 255, 0), (segment[0], segment[1], 20, 20))
        pygame.draw.rect(self.window, (255, 0, 0), (self.food.position[0], self.food.position[1], 20, 20))

if __name__ == '__main__':
    game = Game(window)
    game.run()
    pygame.quit()
    sys.exit()
