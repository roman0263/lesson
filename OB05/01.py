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



run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX -50
            image_rect.y = mouseY -50

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)

    pygame.display.flip()


pygame.quit()
