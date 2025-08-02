import asyncio
import pygame
import time
from globals import *
from Sprites.baskets import basket

async def level():


    # Time
    start_time = time.time()
    clock = pygame.time.Clock()

    run = True
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.load("assets/music/song1.mp3")
    pygame.mixer.music.play()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True

        SCREEN.fill((0,0,0))
        baskets.draw(SCREEN)
        squirrels.draw(SCREEN)
        for nut in nuts:
            nut.move()
        nuts.draw(SCREEN)
        pygame.display.flip()
        await asyncio.sleep(0)
    
    if quit:
        return "quit"