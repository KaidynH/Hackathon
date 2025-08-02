import pygame

class Music(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,music):
        super().__init__()
        # Load image and rect
        self.music = music
        self.volume = 0.2
        self.playing = False
    def load(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load("music/" + self.music + ".ogg")
        pygame.mixer.music.play()