import pygame
import globals as g
from random import randint
import math

class image(pygame.sprite.Sprite):
    def __init__(self, pos, size, img, rot=0):
        super().__init__()

        # Image initialize
        self.image = pygame.image.load(f"graphics/{img}")

        # Image transformation
        self.image = pygame.transform.scale(self.image, size)
        self.image = pygame.transform.rotate(self.image, rot)

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1] 
        self.x = pos[0]
        self.y = pos[1]

        # Movements
        self.speed = 0
        self.y_speed = 0
        self.x_speed = 0

    def set_image(self, img):
        self.image = img

    def draw(self):
        g.SCREEN.blit(self.image, self.rect)

    def shake(self, xseverity=5, yseverity=5, x=None, y=None):
        if (x==None) and (y==None):
            x = randint(-xseverity, xseverity)
            y = randint(-yseverity, yseverity)
        self.rect.centerx += x
        self.rect.centery += y
        return x,y

    def set_glide(self, frame_duration, start, glide_to):
        x_change = glide_to[0] - start[0]
        y_change = glide_to[1] - start[1]
        self.x_speed = math.ceil(x_change/frame_duration)
        self.y_speed = math.ceil(y_change/frame_duration)

    def glide(self, glide_to, deadzone=1):
        if ((self.rect.centerx < (glide_to[0]-deadzone)) or self.rect.centerx > (glide_to[0]+deadzone)) or ((self.rect.centery < (glide_to[1]-deadzone)) or self.rect.centery > (glide_to[1]+deadzone)):
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            return True
        self.rect.center = glide_to
        return False
    
    def get_pos(self):
        return (self.rect.centerx, self.rect.centery)