import pygame
import Sprites.nuts as nut
import globals as g

class squirrel(pygame.sprite.Sprite):
    def __init__(self, pos, img = "squirrel", imgnut = "squirrelnut"):
        super().__init__()

        # Image initialize
        self.width = 50
        self.images = [self.set_image(img), self.set_image(imgnut)]
        self.image = self.images[1]

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.pos = pos

        # Nuts
        self.counter = 0
        self.threw_nut = False

    def reset(self):
        self.__init__(self.pos)
    
    def set_image(self, img):
        # Image initialize
        image = pygame.image.load(f"graphics/{img}.png")
        
        # Size transformation
        original_width, original_height = image.get_size()
        aspect_ratio = original_width / original_height
        self.height = int(self.width / aspect_ratio)
        image = pygame.transform.smoothscale(image, (self.width,self.height))
        return image

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
    