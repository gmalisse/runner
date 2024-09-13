import pygame
from sys import exit

pygame.init()

screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, (64, 64, 64))
text_rect = text_surface.get_rect(center=(400, 50))

snail_x_pos = 600
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(snail_x_pos, 300))


player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', text_rect)
    pygame.draw.rect(screen, '#c0e8ec', text_rect, 10)
    screen.blit(text_surface, text_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    keys = pygame.key.get_pressed()
    if player_rect.bottom >= 300 and keys[pygame.K_SPACE]:
        player_gravity = -20

    if player_rect.bottom > 300:
        player_rect.bottom = 300

    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)

