import os
import pygame

dirname = os.path.dirname(__file__)

class Gem(pygame.sprite.Sprite):
    def __init__(self, gem_x=0, gem_y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "graphics", "gem.png"))

        self.rect = self.image.get_rect()

        self.rect.x = gem_x
        self.rect.y = gem_y
