import asyncio
import pygame
import time
from globals import *

async def level():


    # Time
    start_time = time.time()
    clock = pygame.time.Clock()

    run = True
    while run:

        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True


        pygame.display.flip()
        await asyncio.sleep(0)
    
    if quit:
        return "quit"