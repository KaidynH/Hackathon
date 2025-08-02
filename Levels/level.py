import asyncio
import pygame
import time
from globals import *
import json

async def level():
    # Score
    nuts_collected = 0

    # Time
    start_time = time.time()
    clock = pygame.time.Clock()

    # Start music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.load("music/song1.mp3")
    pygame.mixer.music.play()

    file = open('beatmap.json', 'r')
    beats = json.load(file)
    beat_index = 0
    print(len(beats))
    # Runner variable
    run = True
    while run:
        # Update fps
        clock.tick(FPS)

        current_time = time.time() - start_time
        if beats[beat_index] - 0.031 <= current_time and beats[beat_index] + 0.031 >= current_time and beat_index < len(beats)-1:
            # print("----" if beat_index % 2 == 0 else "beat" if beat_index%3 == 0 else "..")
            print(beat_index)
            beat_index += 1
        elif current_time > beats[beat_index] and beat_index < len(beats)-1:
            beat_index += 1
            print("miss", beat_index)


        
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
                if event.key == pygame.K_i:
                    collided_nut = pygame.sprite.spritecollideany(i_hitbox, nuts)
                    if collided_nut:
                        nuts.remove(collided_nut)

        # Screen updates
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