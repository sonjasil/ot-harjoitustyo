import pygame
from app.back import Back

class Grid:
    def __init__(self, map, cell_size):
        self.cell_size = cell_size
        self.size = len(map)
        self.backs = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(map)

    def _initialize_sprites(self, map):
        height = len(map)
        width = len(map[0])

        for y in range(height):
            for x in range(width):
                cell = map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.backs.add(Back(normalized_x, normalized_y))
            
            self.all_sprites.add(self.backs)