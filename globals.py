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

# Sprites
baskets = pygame.sprite.Group(
    basket((WIDTH * 0.2, HEIGHT - 100)),
    basket((WIDTH * 0.4, HEIGHT - 100)),
    basket((WIDTH * 0.6, HEIGHT - 100)),
    basket((WIDTH * 0.8, HEIGHT - 100))
)

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