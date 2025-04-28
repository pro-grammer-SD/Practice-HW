import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Score Game")

clock = pygame.time.Clock()

player_color = (0, 255, 0)
enemy_color = (255, 0, 0)
bg_color = (0, 0, 0)

player_size = 50
enemy_size = 50

player = pygame.Rect(screen_width // 2, screen_height // 2, player_size, player_size)

enemies = []
for _ in range(7):
    x = random.randint(0, screen_width - enemy_size)
    y = random.randint(0, screen_height - enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

score = 0
font = pygame.font.SysFont(None, 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, screen_width - enemy_size)
            enemy.y = random.randint(0, screen_height - enemy_size)

    screen.fill(bg_color)

    pygame.draw.rect(screen, player_color, player)
    for enemy in enemies:
        pygame.draw.rect(screen, enemy_color, enemy)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
