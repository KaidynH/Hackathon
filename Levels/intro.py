import asyncio
import pygame
from globals import *
import helpers as h

async def intro():

    # Time
    clock = pygame.time.Clock()
    frame = 1

    # Sound effects
    note = pygame.mixer.Sound("music/note.ogg")
    rustling = pygame.mixer.Sound("music/leaves.ogg")
    rustling.play()

    # Animation sprites
    bg_animation = image((66,659), (2598, 1465), "forest.png")
    branch_animation = image((300, 250), (1117, 321), "branch.png")
    nut_animation = image((300, 345), (320,320), "acorn.png")
    basket_animation = image((300, 1082), (150,150), "baskets/basket0.png")
    start_screen = image((300, -400), (600,800), "startScreen.png")
    play_button = button((300, 332), "play.png", (320,90))
    animations = pygame.sprite.Group(bg_animation, branch_animation, nut_animation, basket_animation, start_screen)

    # Basket ending image
    basket_nut = pygame.image.load("graphics/baskets/basket1.png")
    basket_nut = pygame.transform.scale(basket_nut, (150,150))

    # Init variables
    fall_init = False
    nut_glide = (0,0)
    branch_glide = (0,0)
    bg_glide = (0,0)
    basket_glide = (0,0)
    end_init = False
    start_glide = (0,0)
    done_animation = False

    # Runner variable
    run = True
    quit = False
    while run:
        # Update fps
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True            


        # Shaking animation
        if frame <= 45:
            x,y = branch_animation.shake()
            nut_animation.shake(x=x, y=y)

        # Nut falling animation
        elif frame <= 90:
            if not fall_init:
                curr_pos = nut_animation.get_pos()
                nut_glide = (curr_pos[0], 640)
                nut_animation.set_glide(47, curr_pos, nut_glide)

                curr_pos = branch_animation.get_pos()
                branch_glide = (curr_pos[0], -500)
                branch_animation.set_glide(47, curr_pos, branch_glide)

                curr_pos = bg_animation.get_pos()
                bg_glide = (curr_pos[0], 17)
                bg_animation.set_glide(47, curr_pos, bg_glide)

                basket_animation.rect.centerx = nut_animation.rect.centerx
                curr_pos = basket_animation.get_pos()
                basket_glide = (curr_pos[0], 640)
                basket_animation.set_glide(47, curr_pos, basket_glide)

                fall_init = True
            bg_animation.glide(bg_glide)
            nut_animation.glide(nut_glide)
            branch_animation.glide(branch_glide)
            basket_animation.glide(basket_glide)

        # Starting panel comes down
        else:
            if not end_init:
                animations.remove(nut_animation)
                basket_animation.set_image(basket_nut)
                note.play()

                curr_pos = start_screen.get_pos()
                start_glide = (curr_pos[0], 450)
                start_screen.set_glide(47, curr_pos, start_glide)

                end_init = True

            if not done_animation:
                if not start_screen.glide(start_glide, deadzone=10):
                    animations.add(play_button)
                    done_animation = True
            else:
                # Check if play button is pressed
                if play_button.is_clicked():
                    run = False

        animations.draw(SCREEN)

        frame += 1

        pygame.display.flip()

        await asyncio.sleep(0)
    
    await h.fade_out_animation(clock)

    if quit:
        return "quit"
    else:
        return "continue"