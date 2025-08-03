import asyncio
import pygame
import time
from globals import *
import json
import helpers as h

async def level():
    # Score
    nuts_collected = 0

    # Time
    start_time = time.time()
    clock = pygame.time.Clock()
    frame = 1

    beats = h.load_beats("level1.json")

    # Start music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    print(len(beats))
    # Runner variable
    run = True
    while run:
        # Update fps
        clock.tick(FPS)

        current_time = time.time() - start_time


        
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            
            if event.type == pygame.KEYDOWN:
                # Nut collection
                # When a key is pressed, check if nut is colliding with correlating basket
                if event.key == pygame.K_f:
                    collided_nut = pygame.sprite.spritecollideany(f_hitbox, nuts)
                    if collided_nut:
                        nuts.remove(collided_nut)
                if event.key == pygame.K_g:
                    collided_nut = pygame.sprite.spritecollideany(g_hitbox, nuts)
                    if collided_nut:
                        nuts.remove(collided_nut)
                if event.key == pygame.K_h:
                    collided_nut = pygame.sprite.spritecollideany(h_hitbox, nuts)
                    if collided_nut:
                        nuts.remove(collided_nut)
                if event.key == pygame.K_j:
                    collided_nut = pygame.sprite.spritecollideany(j_hitbox, nuts)
                    if collided_nut:
                        nuts.remove(collided_nut)

        # Screen updates
        h.create_nuts(pygame.mixer.music.get_pos(), beats)

        SCREEN.fill((0,0,0))

        baskets.draw(SCREEN)
        squirrels.draw(SCREEN)
        for nut in nuts:
            nut.move()
        nuts.draw(SCREEN)

        frame += 1

        pygame.display.flip()

        await asyncio.sleep(0)
    
    if quit:
        return "quit"