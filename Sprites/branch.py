import pygame
import globals as g

class branch(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Image initialize
        self.image = pygame.image.load("graphics/branch.png")

        # Size transformation
        self.width = 640
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        self.height = int(self.width / aspect_ratio)
        self.image = pygame.transform.smoothscale(self.image, (self.width,self.height))

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1] 

    def draw(self):
        g.SCREEN.blit(self.image, self.rect)