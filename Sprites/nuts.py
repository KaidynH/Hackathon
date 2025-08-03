import pygame
import globals as g


class nut(pygame.sprite.Sprite):
    speed = 10

    def __init__(self, pos):
        super().__init__()

        # Image initialize
        self.image = g.nuts_image

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.dropped = False

    
    def move(self):
        self.rect.centery += nut.speed
        if self.rect.top >= g.HEIGHT:
            self.kill()

    def fail(self, sound:pygame.mixer.Sound):
        if not self.dropped:
            self.dropped = True
            sound.play()
            sound.set_volume(3)