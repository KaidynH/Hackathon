import asyncio
import pygame
from globals import *
import helpers as h

async def ending(stats):
    # Stats
    score = stats["score"]
    combo = stats["combo"]
    collected = stats["collected"]
    total = stats["total"]

    # Text
    score_txt = font.render(f"Score: {score}", True, (41, 122, 83))
    combo_txt = font.render(f"Highest Combo: {combo}", True, (41, 122, 83))
    collected_txt = font.render(f"Acorns Collected: {collected}/{total}", True, (41, 122, 83))

    # Stats background
    wood = pygame.image.load("graphics/end.png")
    width = 400
    original_width, original_height = wood.get_size()
    aspect_ratio = original_width / original_height
    height = int(width / aspect_ratio)
    wood = pygame.transform.smoothscale(wood, (width,height))

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
            
        # Screen updates
        squirrels.update()
        SCREEN.blit(background, (0,-100))
        baskets.draw(SCREEN)

        SCREEN.blit(wood, (100, 270))
        SCREEN.blit(score_txt, (140, 290))
        SCREEN.blit(combo_txt, (140, 330))
        SCREEN.blit(collected_txt, (140, 370))
        
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
    pygame.mixer.music.unload()

    if quit:
        return "quit"
    else:
        return "restart" if restart else "end"