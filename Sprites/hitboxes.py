import pygame

class hitbox(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.size = 30
        self.rect = pygame.Rect(pos[0], pos[1], self.size, self.size)