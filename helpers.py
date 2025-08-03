import json
from globals import *
import Sprites.nuts as Nuts
from random import randint
import asyncio

squirrels_list = squirrels.sprites()

def create_nuts(music_pos:int, beats:list):
    if len(beats) > 0:
        offset = (basket_height - nuts_height) / Nuts.nut.speed
        offset /= FPS
        music_pos /= 1000.00
        if (music_pos + offset) >= beats[0]:
            n = randint(1,4)
            x = WIDTH * n * 0.2
            nuts.add(Nuts.nut((x, nuts_height)))
            return beats.pop(0)
    return False

def load_beats(music_data:str):
    file = open(f"music/{music_data}")
    data = json.load(file)
    file.close()
    return data["beats"]

def fade_out(fade_level):
    alpha = fade_level + FADE_FACTOR
    if alpha > 100:
        return 100
    FADE_SURFACE.fill((0,0,0, alpha))
    SCREEN.blit(FADE_SURFACE, (0,0))
    return alpha

def fade_in(fade_level):
    alpha = fade_level - FADE_FACTOR
    if alpha < 0:
        return 0
    FADE_SURFACE.fill((0,0,0, alpha))
    SCREEN.blit(FADE_SURFACE, (0,0))
    return alpha

async def fade_out_animation(clock):
    fade = 0
    while fade < 100:
        clock.tick(FPS)
        fade = fade_out(fade)
        pygame.display.flip()
        await asyncio.sleep(0)

def fade_in_animation(fade):
    if fade > 0:
        fade = fade_in(fade)
    # pygame.display.flip()
    return fade