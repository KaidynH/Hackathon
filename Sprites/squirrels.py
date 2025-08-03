import pygame
import Sprites.nuts as nut
import globals as g
import random

class squirrel(pygame.sprite.Sprite):
    def __init__(self, pos, instrument):
        super().__init__()

        self.instrument = instrument

        # Image initialize
        self.width = 50
        self.image_paths = [f"graphics/squirrels/{instrument}s/{instrument}{i}.png" for i in range(3)]
        self.image_index = 0
        self.images = [pygame.image.load(self.image_paths[i]) for i in range(3)]
        
        # Resize
        self.width = 75
        for i in range(3):
            img = self.images[i]
            original_width, original_height = img.get_size()
            aspect_ratio = original_width / original_height
            self.height = int(self.width / aspect_ratio)
            if instrument == "mic" or instrument == "trumpet":
                img = pygame.transform.flip(img, True, False)
            self.images[i] = pygame.transform.smoothscale(img, (self.width,self.height))

        self.image = self.images[0]

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.pos = pos


        # Nuts
        self.counter = 0
        self.threw_nut = False

    def reset(self):
        self.__init__(self.pos, self.instrument)

    def unload_nut(self):
        self.counter = 0
        self.image = self.images[0]
        self.threw_nut = True

    def update(self):
        if self.threw_nut:
            self.counter += 1
            if self.counter == 15:
                self.threw_nut = False
                self.image = self.images[1]
        if random.randint(1, 5) == 1:
            self.image_index = (self.image_index + 1) % 3
            self.image = self.images[self.image_index]
    