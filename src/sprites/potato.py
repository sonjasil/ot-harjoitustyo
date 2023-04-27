import os
import pygame

dirname = os.path.dirname(__file__)

class Potato(pygame.sprite.Sprite):
    def __init__(self, p_x=0, p_y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "graphics", "potato.png"))

        self.rect = self.image.get_rect()

        self.rect.x = p_x
        self.rect.y = p_y
