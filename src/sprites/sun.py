import os
import pygame

dirname = os.path.dirname(__file__)


class Sun(pygame.sprite.Sprite):
    def __init__(self, sun_x=0, sun_y=0):
        super().__init__()
        self.id = 9

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "graphics", "sun.png"))

        self.rect = self.image.get_rect()

        self.rect.x = sun_x
        self.rect.y = sun_y
