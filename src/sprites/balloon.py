import os
import pygame

dirname = os.path.dirname(__file__)

class Balloon(pygame.sprite.Sprite):
    def __init__(self, balloon_x=0, balloon_y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "graphics", "balloon.png"))

        self.rect = self.image.get_rect()

        self.rect.x = balloon_x
        self.rect.y = balloon_y
