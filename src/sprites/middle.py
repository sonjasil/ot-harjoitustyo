import os
import pygame

dirname = os.path.dirname(__file__)


class Middle(pygame.sprite.Sprite):
    def __init__(self, mid_x=0, mid_y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "graphics", "middle.png"))

        self.rect = self.image.get_rect()

        self.rect.x = mid_x
        self.rect.y = mid_y
