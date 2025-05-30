import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

bg_color = (58, 58, 58)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
image = pygame.image.load("./assets/image1.png")
image = pygame.transform.scale(image, (300, 300))

x = (500 - 300) // 2
y = (500 - 300) // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    screen.blit(image, (x, y))
    pygame.display.flip()
