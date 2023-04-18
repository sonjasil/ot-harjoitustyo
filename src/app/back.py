import os
import pygame

dirname = os.path.dirname(__file__)

class Back(pygame.sprite.Sprite):
    def __init__(self, back_x=0, back_y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "graphics", "back200.png"))

        self.rect = self.image.get_rect()

        self.rect.x = back_x
        self.rect.y = back_y
