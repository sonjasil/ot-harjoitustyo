import os
import pygame

dirname = os.path.dirname(__file__)


class Tulip(pygame.sprite.Sprite):
    def __init__(self, tulip_x=0, tulip_y=0):
        super().__init__()
        self.id = 10

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "graphics", "tulip.png"))

        self.rect = self.image.get_rect()

        self.rect.x = tulip_x
        self.rect.y = tulip_y
