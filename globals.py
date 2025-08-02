import pygame
from Sprites.baskets import basket
from Sprites.squirrels import squirrel
from Sprites.nuts import nut
from Sprites.hitboxes import hitbox

# Screen setup
WIDTH = 600
HEIGHT = 800
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hackathon")

# Frames timing
FPS = 30

# Music
VOLUME = 0.2

# Sprites
f_basket = basket((WIDTH * 0.2, HEIGHT - 100))
g_basket = basket((WIDTH * 0.4, HEIGHT - 100))
h_basket = basket((WIDTH * 0.6, HEIGHT - 100))
i_basket = basket((WIDTH * 0.8, HEIGHT - 100))

f_hitbox = hitbox((f_basket.rect.centerx-15, f_basket.rect.centery-15))
g_hitbox = hitbox((g_basket.rect.centerx-15, g_basket.rect.centery-15))
h_hitbox = hitbox((h_basket.rect.centerx-15, h_basket.rect.centery-15))
i_hitbox = hitbox((i_basket.rect.centerx-15, i_basket.rect.centery-15))

baskets = pygame.sprite.Group(f_basket, g_basket, h_basket, i_basket)

hitboxes = pygame.sprite.Group(f_hitbox, g_hitbox, h_hitbox, i_hitbox)

squirrels = pygame.sprite.Group(
    squirrel((WIDTH * 0.2, 200)),
    squirrel((WIDTH * 0.4, 200)),
    squirrel((WIDTH * 0.6, 200)),
    squirrel((WIDTH * 0.8, 200))
)

nuts = pygame.sprite.Group(
    nut((WIDTH * 0.2, 200)),
    nut((WIDTH * 0.4, 200)),
    nut((WIDTH * 0.6, 200)),
    nut((WIDTH * 0.8, 200))
)