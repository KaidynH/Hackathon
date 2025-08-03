import pygame
import os

class basket(pygame.sprite.Sprite):
    def __init__(self, pos, key=""):
        super().__init__()

        self.key = key
        # Image initialize
        self.image_paths = [f"graphics/baskets/{key}/{key}{i}.png" for i in range(4)]
        self.image_index = 0
        self.images = [pygame.image.load(self.image_paths[i]) for i in range(4)]

        # Resize
        self.width = 80
        for i in range(4):
            img = self.images[i]
            original_width, original_height = img.get_size()
            aspect_ratio = original_width / original_height
            self.height = int(self.width / aspect_ratio)
            self.images[i] = pygame.transform.smoothscale(img, (self.width,self.height))
        
        self.image = self.images[0]

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1] 
        self.pos = pos

        # Number of nuts collected
        self.nuts = 0

    def reset(self):
        self.__init__(self.pos, self.key)

    def update_image(self):
        self.image_index += 1
        self.image = self.images[self.image_index]
    