import asyncio
import pygame
import Levels.level as level
import Levels.intro as intro
import Levels.ending as ending
from globals import *

async def main():
    playing = True

    status = await intro.intro()
    if status == "quit":
        return
    
    while playing:
        stats = await level.level()
        if stats == "quit":
            return
        
        status = await ending.ending(stats)
        if status == "quit":
            return
        playing = status == "restart"

# Run the game
asyncio.run(main())