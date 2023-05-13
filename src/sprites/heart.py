import os
import pygame

dirname = os.path.dirname(__file__)


class Heart(pygame.sprite.Sprite):
    def __init__(self, heart_x=0, heart_y=0):
        super().__init__()
        self.id = 5

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "graphics", "heart.png"))

        self.rect = self.image.get_rect()

        self.rect.x = heart_x
        self.rect.y = heart_y
