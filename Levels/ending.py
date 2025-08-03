import asyncio
import pygame
import time
from globals import *
import json
import helpers as h

async def ending():
    print("ENDING")

    # Time
    clock = pygame.time.Clock()
    frame = 1

    # Start music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.load("music/song1.ogg")
    pygame.mixer.music.play()

    # Background image
    background = pygame.image.load("graphics/forest.png")
    fade = 255
    fg.add(restart_btn)

    # Runner variable
    run = True
    quit = False
    restart = False
    while run:
        # Update fps
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    quit = True
            
        # Screen updates
        SCREEN.blit(background, (0,-100))
        baskets.draw(SCREEN)
        fg.draw(SCREEN)
        squirrels.draw(SCREEN)

        if restart_btn.is_clicked():
            restart = True
            run = False

        frame += 1

        fade = h.fade_in_animation(fade)

        pygame.display.flip()

        await asyncio.sleep(0)
    
    await h.fade_out_animation(clock)

    if quit:
        return "quit"
    else:
        return "restart" if restart else "end"