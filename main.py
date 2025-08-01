import asyncio
import pygame
import Levels.level as level
from globals import *

# Unknown issue with setting up screen in globals
# Set up here instead
WIDTH = 600
HEIGHT = 1000
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hackathon")

async def main():

    # status = await level.level()
    # if status == "quit":
    #     return
    status = await level.level()

# Run the game
asyncio.run(main())