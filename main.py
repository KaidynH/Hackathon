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
        status = await level.level()
        if status == "quit":
            return
        print("STATUS:", status)
        
        status = await ending.ending()
        if status == "quit":
            return
        playing = status == "restart"

# Run the game
asyncio.run(main())