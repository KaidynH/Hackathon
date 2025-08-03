import pygame
from Sprites.baskets import basket
from Sprites.squirrels import squirrel
from Sprites.nuts import nut
from Sprites.hitboxes import hitbox
from Sprites.buttons import button
from Sprites.branch import branch
from Sprites.image import image

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

# Fade screen
FADE_SURFACE = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
FADE_FACTOR = 5

# Text
font = pygame.font.Font("fonts/Orbitron-Medium.ttf", 22)

# Heights
basket_height = HEIGHT - 100
nuts_height = 200

# Sprites
f_basket = basket((WIDTH * 0.2, basket_height))
g_basket = basket((WIDTH * 0.4, basket_height))
h_basket = basket((WIDTH * 0.6, basket_height))
j_basket = basket((WIDTH * 0.8, basket_height))

f_hitbox = hitbox((f_basket.rect.centerx-15, f_basket.rect.centery-15))
g_hitbox = hitbox((g_basket.rect.centerx-15, g_basket.rect.centery-15))
h_hitbox = hitbox((h_basket.rect.centerx-15, h_basket.rect.centery-15))
j_hitbox = hitbox((j_basket.rect.centerx-15, j_basket.rect.centery-15))

baskets = pygame.sprite.Group(f_basket, g_basket, h_basket, j_basket)

hitboxes = pygame.sprite.Group(f_hitbox, g_hitbox, h_hitbox, j_hitbox)

squirrels = pygame.sprite.Group(
    squirrel((WIDTH * 0.2, 200)),
    squirrel((WIDTH * 0.4, 200)),
    squirrel((WIDTH * 0.6, 200)),
    squirrel((WIDTH * 0.8, 200))
)

nuts = pygame.sprite.Group()

start_btn = button((WIDTH//2, HEIGHT//2), "start.png", (200,200))

fg = pygame.sprite.Group(
    start_btn
)

tree = branch((300, 200))

keys = [
    {"key": pygame.K_f, "hitbox": f_hitbox},
    {"key": pygame.K_g, "hitbox": g_hitbox},
    {"key": pygame.K_h, "hitbox": h_hitbox},
    {"key": pygame.K_j, "hitbox": j_hitbox}
]