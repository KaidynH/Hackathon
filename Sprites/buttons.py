import pygame
import globals as g


class button(pygame.sprite.Sprite):
    def __init__(self, pos, img, size):
        super().__init__()

        # Image initialize
        self.image = pygame.image.load(f"graphics/{img}")
        self.image = pygame.transform.scale(self.image, size)

        # Set position
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]