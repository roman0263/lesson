import pygame
import random

pygame.init()

# Определение констант
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_SIZE = 20
BRICK_WIDTH, BRICK_HEIGHT = 75, 30

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Классы игровых объектов
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) / 2, SCREEN_HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 5

    def move(self, direction):
        if direction == "left":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        elif direction == "right":
            self.rect.x += self.speed
            if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
                self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect((SCREEN_WIDTH - BALL_SIZE) / 2, SCREEN_HEIGHT / 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = 3 * random.choice((-1, 1))
        self.speed_y = -3

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - BALL_SIZE:
            self.speed_x *= -1
        if self.rect.y <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, RED, self.rect)

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.is_active = True

    def draw(self, screen):
        if self.is_active:
            pygame.draw.rect(screen, BLUE, self.rect)

# Инициализация Pygame и создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Арканоид")
clock = pygame.time.Clock()

# Создание игровых объектов
paddle = Paddle()
ball = Ball()
bricks = [Brick(x * (BRICK_WIDTH + 10), y * (BRICK_HEIGHT + 5)) for x in range(10) for y in range(5)]

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")

    ball.move()

    # Обработка столкновений
    if paddle.rect.colliderect(ball.rect):
        ball.speed_y *= -1

    for brick in bricks:
        if brick.is_active and brick.rect.colliderect(ball.rect):
            brick.is_active = False
            ball.speed_y *= -1

    # Очистка экрана и рисование
    screen.fill((0, 0, 0))
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
