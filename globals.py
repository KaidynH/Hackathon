import pygame
from Sprites.baskets import basket
from Sprites.squirrels import squirrel
from Sprites.nuts import nut

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

# Heights
basket_height = HEIGHT - 100
nuts_height = 200

# Sprites
baskets = pygame.sprite.Group(
    basket((WIDTH * 0.2, basket_height)),
    basket((WIDTH * 0.4, basket_height)),
    basket((WIDTH * 0.6, basket_height)),
    basket((WIDTH * 0.8, basket_height))
)

squirrels = pygame.sprite.Group(
    squirrel((WIDTH * 0.2, 200)),
    squirrel((WIDTH * 0.4, 200)),
    squirrel((WIDTH * 0.6, 200)),
    squirrel((WIDTH * 0.8, 200))
)

nuts = pygame.sprite.Group(
    nut((WIDTH * 0.2, nuts_height)),
    nut((WIDTH * 0.4, nuts_height)),
    nut((WIDTH * 0.6, nuts_height)),
    nut((WIDTH * 0.8, nuts_height))
)