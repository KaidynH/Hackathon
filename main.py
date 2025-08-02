import asyncio
import pygame
import Levels.level as level
from globals import *

async def main():

    status = await level.level()

# Run the game
asyncio.run(main())