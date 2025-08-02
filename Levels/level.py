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

    nuts_beats = h.load_beats("level1.json")
    print(nuts_beats, len(nuts_beats), nuts_beats[80])

    # Start music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.load("music/song1.mp3")
    pygame.mixer.music.play()

    # Sound effects
    wrong_sound = pygame.mixer.Sound("music/wrong1.mp3")
    swoop = pygame.mixer.SoundType("music/swoop.mp3")
    swoop.set_volume(3)

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
                key_pressed = False
                for k in keys:
                    if event.key == k["key"]:
                        key_pressed = True
                        collided_nut = pygame.sprite.spritecollideany(k["hitbox"], nuts)
                        if collided_nut:
                            nuts.remove(collided_nut)
                            break
                else:
                    if key_pressed:
                        wrong_sound.play()

        # Screen updates
        h.create_nuts(pygame.mixer.music.get_pos(), nuts_beats)

        SCREEN.fill((0,0,0))
        squirrels.update()

        baskets.draw(SCREEN)
        squirrels.draw(SCREEN)
        for nut in nuts:
            nut.move()
            if nut.rect.y > j_hitbox.rect.bottom:
                nut.fail(swoop)
                
        nuts.draw(SCREEN)

        frame += 1

        pygame.display.flip()

        await asyncio.sleep(0)
    
    if quit:
        return "quit"