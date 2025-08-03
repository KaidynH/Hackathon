import asyncio
import pygame
import time
from globals import *
import json
import helpers as h

async def level():
    # Score
    nuts_collected = 0
    nuts_total = 0
    streak = 0
    streak_txt = font.render(f"Score: {streak}", True, "white")
    score_txt = font.render(f"Streak: {nuts_collected}", True, "white")

    # Time
    clock = pygame.time.Clock()
    frame = 1

    # Nuts timing
    nuts_beats = h.load_beats("level1.json")
    print(nuts_beats, len(nuts_beats), nuts_beats[80])

    # Start music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.load("music/song2.mp3")
    pygame.mixer.music.play()

    # Sound effects
    wrong_sound = pygame.mixer.Sound("music/wrong.mp3")
    swoop = pygame.mixer.SoundType("music/swoop.mp3")
    swoop.set_volume(3)

    file = open('beatmap.json', 'r')
    beats = json.load(file)
    beat_index = 0
    print(len(beats))

    # Background image
    background = pygame.image.load("graphics/background.png")

    # Runner variable
    run = True
    playing = False
    quit = False
    while run:
        # Update fps
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            
            if event.type == pygame.KEYDOWN:
                # Nut collection
                # When a key is pressed, check if nut is colliding with correlating basket
                if playing:
                    key_pressed = False
                    for k in keys:
                        if event.key == k["key"]:
                            key_pressed = True
                            collided_nut = pygame.sprite.spritecollideany(k["hitbox"], nuts)
                            if collided_nut:
                                nuts.remove(collided_nut)
                                nuts_collected += 1
                                streak += 1
                                print(nuts_collected)
                                break
                    else:
                        if key_pressed:
                            wrong_sound.play()

        if playing:
            # beat
            current_time = time.time() - start_time
            if beats[beat_index] - 0.031 <= current_time and beats[beat_index] + 0.031 >= current_time and beat_index < len(beats)-1:
                # print("----" if beat_index % 2 == 0 else "beat" if beat_index%3 == 0 else "..")
                # print(beat_index)
                beat_index += 1
            elif current_time > beats[beat_index] and beat_index < len(beats)-1:
                beat_index += 1
                # print("miss", beat_index)

            # Drop nuts
            if h.create_nuts(pygame.mixer.music.get_pos(), nuts_beats):
                nuts_total += 1

            squirrels.update()
            for nut in nuts:
                nut.move()
                if nut.rect.y > j_hitbox.rect.bottom:
                    nut.fail(swoop)  
                    streak = 0
            score_txt = font.render(f"Score: {nuts_collected}", True, "white")
            streak_txt = font.render(f"Streak: {streak}", True, "white")

        else:
            if start_btn.is_clicked():
                playing = True
                pygame.mixer.music.unload()
                pygame.mixer.music.load("music/song1.mp3")
                pygame.mixer.music.play()
                start_time = time.time()
                fg.remove(start_btn)

        
        # Screen updates
        # SCREEN.fill((0,0,0))
        SCREEN.blit(background, (0,0))
        baskets.draw(SCREEN)
        squirrels.draw(SCREEN)
        nuts.draw(SCREEN)
        fg.draw(SCREEN)
        SCREEN.blit(score_txt, (450, 30))
        SCREEN.blit(streak_txt, (450, 60))

        frame += 1

        if not pygame.mixer.music.get_busy():
            run = False

        pygame.display.flip()

        await asyncio.sleep(0)
    
    if quit:
        return "quit"
    else:
        return (nuts_collected, nuts_total, nuts_collected/nuts_total)