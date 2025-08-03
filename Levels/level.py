import asyncio
import pygame
from globals import *
import helpers as h

async def level():
    # Score
    points_per_nut = 5
    nuts_collected = 0
    nuts_total = 0
    score = 0
    streak = 0
    high_streak = 0
    multiplier = 1
    score_txt = font.render(f"Score: {score}", True, "white")
    streak_txt = font.render(f"Streak: {streak}", True, "white")

    # Time
    clock = pygame.time.Clock()
    frame = 1
    counter = 1

    beats = h.load_beats("level1.json")
    nuts_total = len(beats)

    # Start music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.load(song)

    # Sound effects
    wrong_sound = pygame.mixer.Sound("music/wrong.ogg")
    swoop = pygame.mixer.SoundType("music/swoop.ogg")
    swoop.set_volume(3)

    # Background image
    background = pygame.image.load("graphics/forest.png")
    fade = 255
    fg.empty()
    fg.add(tree)

    # Sprites edit
    for s in squirrels:
        s.reset()
    for b in baskets:
        b.reset()
    nuts.empty()

    # Runner variable
    run = True
    quit = False
    start = False
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
                key_pressed = False
                for k in keys:
                    if event.key == k["key"]:
                        key_pressed = True
                        collided_nut = pygame.sprite.spritecollideany(k["hitbox"], nuts)
                        if collided_nut:
                            # Remove nut
                            nuts.remove(collided_nut)
                            # Update score
                            nuts_collected += 1
                            streak += 1
                            if streak > high_streak:
                                high_streak = streak
                            if streak % 5 == 0 and multiplier < 8:
                                multiplier *= 2
                            score += points_per_nut * multiplier
                            # Update basket
                            basket = k["basket"]
                            basket.nuts += 1
                            if basket.nuts % 2 == 0 and basket.nuts <= 6:
                                basket.update_image()
                            break
                else:
                    # Check if wrong key is pressed
                    if key_pressed:
                        wrong_sound.play()
                        streak = 0
                        multiplier = 1

        if not start:
            # Start playing music
            pygame.mixer.music.play()
            start = True

        # Drop nuts
        h.create_nuts(pygame.mixer.music.get_pos(), beats)

        # Animation
        squirrels.update()
        for nut in nuts:
            nut.move()
            if nut.rect.y > j_hitbox.rect.bottom:
                nut.fail(swoop)  
                streak = 0
                multiplier = 1

        # Score texts        
        score_txt = font.render(str(score), True, "white")
        streak_txt = font.render(f"Combo: {streak}", True, "white")
        multiplier_txt = font.render(f"x{multiplier}", True, "white")
        
        # Screen updates
        h.create_nuts(pygame.mixer.music.get_pos(), beats)

        # SCREEN.fill((0,0,0))
        SCREEN.blit(background, (-30,-40))

        # Draw on screen
        baskets.draw(SCREEN)
        nuts.draw(SCREEN)
        fg.draw(SCREEN)
        squirrels.draw(SCREEN)
        SCREEN.blit(score_txt, (495, 30))
        SCREEN.blit(streak_txt, (450, 60))
        SCREEN.blit(multiplier_txt, (455, 30))

        frame += 1

        # End game
        if (len(beats) == 0):
            counter += 1
            if counter >= 120:
                run = False

        fade = h.fade_in_animation(fade)

        pygame.display.flip()
        
        await asyncio.sleep(0)
    
    await h.fade_out_animation(clock)
    pygame.mixer.music.unload()

    if quit:
        return "quit"
    else:
        return {"collected":nuts_collected, "total":nuts_total, "combo":high_streak, "score":score}