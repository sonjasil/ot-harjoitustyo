import os
import pygame

dirname = os.path.dirname(__file__)

class Apple(pygame.sprite.Sprite):
    def __init__(self, apple_x=0, apple_y=0):
        super().__init__()
        self.id = 1

        self.image = pygame.image.load(os.path.join(dirname, "..", "graphics", "apple.png"))

        self.rect = self.image.get_rect()

        self.rect.x = apple_x
        self.rect.y = apple_y
