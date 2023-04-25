import os
import pygame

dirname = os.path.dirname(__file__)

class Star(pygame.sprite.Sprite):
    def __init__(self, star_x=0, star_y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "graphics", "star.png"))

        self.rect = self.image.get_rect()

        self.rect.x = star_x
        self.rect.y = star_y
