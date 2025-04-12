import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

bg_color = (255, 255, 255)
rect_color = (0, 128, 255)
rect_width, rect_height = 200, 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2

font = pygame.font.SysFont(None, 48)
text = font.render("Hello, Pygame!", True, (0, 0, 0))
text_rect = text.get_rect(center=(320, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    screen.blit(text, text_rect)
    pygame.display.flip()
