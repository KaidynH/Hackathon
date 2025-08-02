import asyncio
import pygame
import Levels.level as level
from globals import *

async def main():

    status = await level.level()
    print(status)

# Run the game
asyncio.run(main())