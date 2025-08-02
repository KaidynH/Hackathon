import asyncio
import pygame
import Levels.level as level
from globals import *
import os
# print("Current working directory:", os.getcwd())
# print("File exists:", os.path.isfile("graphics/basket.png"))

# # Unknown issue with setting up screen in globals
# # Set up here instead
WIDTH = 600
HEIGHT = 800
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hackathon")

async def main():

    status = await level.level()

# Run the game
asyncio.run(main())