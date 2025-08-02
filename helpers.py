import json
from globals import *
import Sprites.nuts as Nuts
import math
from random import randint

def create_nuts(frame:int, beats:list):
    if len(beats) > 0:
        offset = (basket_height - nuts_height) / Nuts.nut.speed
        if (frame+offset) == math.floor((beats[0]) * FPS):
            x = WIDTH * randint(1,4) * 0.2
            nuts.add(Nuts.nut((x, nuts_height)))
            return beats.pop(0)
    return False

def load_beats(music_data:str):
    file = open(f"music/{music_data}")
    data = json.load(file)
    file.close()
    return data["beats"]