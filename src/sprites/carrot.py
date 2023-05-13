import os
import pygame

dirname = os.path.dirname(__file__)


class Carrot(pygame.sprite.Sprite):
    def __init__(self, carrot_x=0, carrot_y=0):
        super().__init__()
        self.id = 3

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "graphics", "carrot.png"))

        self.rect = self.image.get_rect()

        self.rect.x = carrot_x
        self.rect.y = carrot_y
