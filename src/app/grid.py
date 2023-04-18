import pygame
from back import Back

class Grid:
    def __init__(self, grid_map, cell_size):
        self.grid_map = grid_map
        self.cell_size = cell_size
        self.size = len(grid_map)
        self.backs = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(grid_map)

    def _initialize_sprites(self, grid_map):
        height = len(grid_map)
        width = len(grid_map[0])

        for grid_y in range(height):
            for grid_x in range(width):
                cell = self.grid_map[grid_y][grid_x]
                normalized_x = grid_x * self.cell_size
                normalized_y = grid_y * self.cell_size

                if cell == 0:
                    self.backs.add(Back(normalized_x, normalized_y))

            self.all_sprites.add(self.backs)
