import json
from globals import *
import Sprites.nuts as Nuts
import Sprites.squirrels as squirrel
import math
from random import randint

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
            squirrels_list[n-1].unload_nut()
            return beats.pop(0)
    return False

def load_beats(music_data:str):
    file = open(f"music/{music_data}")
    data = json.load(file)
    file.close()
    return data["beats"]