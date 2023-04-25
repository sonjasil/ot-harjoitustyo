import os
import pygame

dirname = os.path.dirname(__file__)

class Moon(pygame.sprite.Sprite):
    def __init__(self, moon_x=0, moon_y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "graphics", "moon.png"))

        self.rect = self.image.get_rect()

        self.rect.x = moon_x
        self.rect.y = moon_y
