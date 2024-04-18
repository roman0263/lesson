import pygame
pygame.init()
import os
print("Текущий рабочий каталог:", os.getcwd())

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проэкт")

image = pygame.image.load("picPyton.png")
image = pygame.transform.scale(image, (100, 100))
image_rect = image.get_rect()

speed = 3

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)

    pygame.display.flip()


pygame.quit()
