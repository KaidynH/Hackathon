import pygame
import os

class basket(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Image initialize
        self.image = pygame.image.load("graphics/basket.png")

        # Size transformation
        self.width = 85
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        self.height = int(self.width / aspect_ratio)
        self.image = pygame.transform.smoothscale(self.image, (self.width,self.height))

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1] 
        self.pos = pos

    def reset(self):
        self.__init__(self.pos)