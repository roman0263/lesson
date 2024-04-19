import pygame
import sys

class Game:
    def __init__(self, window, Snake):
        self.window = window
        self.snake = Snake()
        self.food = Food(800, 600, 20)  # Примерные значения для размеров окна и размера ячейки
        self.clock = pygame.time.Clock()  # Таймер для контроля скорости игры

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
            if self.snake.body[-1] == self.food.position:  # Проверка столкновения змейки с едой
                self.snake.grow_up()  # Змейка растет
                self.food.spawn_food()  # Генерация новой еды

            self.window.fill((0, 0, 0))  # Очистка экрана
            # Отрисовка змейки и еды (код отрисовки не представлен)
            pygame.display.flip()  # Обновление экрана

            self.clock.tick(10)  # Контроль скорости игры

        pygame.quit()
        sys.exit()

# Инициализация и запуск игры
pygame.init()
window = pygame.display.set_mode((800, 600))
game = Game(window)
game.run()
