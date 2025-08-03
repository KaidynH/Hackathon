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

# Song
song = "music/song2.mp3"

# Frames timing
FPS = 30

# Music
VOLUME = 0.2

# Nut image
nuts_image = pygame.image.load("graphics/nut.png")
nuts_width = 30
original_width, original_height = nuts_image.get_size()
aspect_ratio = original_width / original_height
nuts_height = int(nuts_width / aspect_ratio)
nuts_image = pygame.transform.smoothscale(nuts_image, (nuts_width,nuts_height))

# Fade screen
FADE_SURFACE = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
FADE_FACTOR = 5

# Text
font = pygame.font.Font("fonts/Orbitron-Medium.ttf", 22)

# Heights
basket_height = HEIGHT - 100
nuts_height = 200
hitbox_offset = 35

# Sprites
f_basket = basket((WIDTH * 0.2, basket_height))
g_basket = basket((WIDTH * 0.4, basket_height))
h_basket = basket((WIDTH * 0.6, basket_height))
j_basket = basket((WIDTH * 0.8, basket_height))

f_hitbox = hitbox((f_basket.rect.centerx-hitbox_offset, f_basket.rect.centery-hitbox_offset))
g_hitbox = hitbox((g_basket.rect.centerx-hitbox_offset, g_basket.rect.centery-hitbox_offset))
h_hitbox = hitbox((h_basket.rect.centerx-hitbox_offset, h_basket.rect.centery-hitbox_offset))
j_hitbox = hitbox((j_basket.rect.centerx-hitbox_offset, j_basket.rect.centery-hitbox_offset))

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
restart_btn = button((WIDTH//2, HEIGHT//2), "restart.png", (200,200))
fg = pygame.sprite.Group()

tree = branch((300, 200))

keys = [
    {"key": pygame.K_f, "hitbox": f_hitbox},
    {"key": pygame.K_g, "hitbox": g_hitbox},
    {"key": pygame.K_h, "hitbox": h_hitbox},
    {"key": pygame.K_j, "hitbox": j_hitbox}
]