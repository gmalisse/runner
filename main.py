import pygame
from sys import exit

pygame.init()

screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600

while True:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 270))
    pygame.display.update()
    clock.tick(60)

