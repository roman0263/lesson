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
        self.body = [(100, 100), (100, 120), (100, 140)]
        self.direction = (0, -20)  # начальное направление движения
        self.grow = False
        self.speed = 20  # Скорость движения змейки

    def move(self):
        if not self.grow:
            self.body.pop(0)  # Удаляем последний элемент тела, если змейка не растет
        self.grow = False

        head_x, head_y = self.body[-1]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.append(new_head)  # Добавляем новую голову

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]):
            self.direction = (new_direction[0] * self.speed, new_direction[1] * self.speed)  # Изменяем направление с учетом скорости

    def check_collision(self):
        head = self.body[-1]
        return head in self.body[:-1]

    def grow_up(self):
        self.grow = True  # Змейка будет расти при следующем вызове move()

class Food:
    def __init__(self, window_width, window_height, cell_size, snake):
        self.window_width = window_width
        self.window_height = window_height
        self.cell_size = cell_size
        self.snake = snake
        self.position = self.spawn_food()

    def spawn_food(self):
        while True:
            x = random.randint(0, (self.window_width - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.window_height - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake.body:
                return (x, y)  # Гарантируем, что еда не появится на теле змейки

class Game:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width  # Добавляем это поле
        self.window_height = window_height  # Добавляем это поле
        self.snake = Snake()
        self.food = Food(window_width, window_height, 20, self.snake)
        self.clock = pygame.time.Clock()

    def check_wall_collision(self):
        head_x, head_y = self.snake.body[-1]
        # Используем атрибуты класса для проверки столкновения
        if head_x < 0 or head_x >= self.window_width or head_y < 0 or head_y >= self.window_height:
            return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((1, 0))

            self.snake.move()
            if self.snake.body[-1] == self.food.position:
                self.snake.grow_up()
                self.food.position = self.food.spawn_food()

            if self.check_wall_collision():
                print("Столкновение со стеной! Игра окончена.")
                running = False

            self.window.fill((0, 0, 0))
            self.draw_objects()
            pygame.display.flip()
            self.clock.tick(10)

    def draw_objects(self):
        for segment in self.snake.body:
            pygame.draw.rect(self.window, (0, 255, 0), (segment[0], segment[1], 20, 20))
        pygame.draw.rect(self.window, (255, 0, 0), (self.food.position[0], self.food.position[1], 20, 20))

if __name__ == '__main__':
    game = Game(window, window_width, window_height)
    game.run()
    pygame.quit()
    sys.exit()
