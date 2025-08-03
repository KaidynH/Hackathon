import asyncio
import pygame
import Levels.level as level
import Levels.intro as intro
from globals import *

async def main():

    status = await intro.intro()
    if status == "quit":
        return

    status = await level.level()
    print(status)

# Run the game
asyncio.run(main())