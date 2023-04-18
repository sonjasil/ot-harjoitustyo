import pygame
from grid import Grid

def create_map(level):
    if level == 1:
        map_grid = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    elif level == 2:
        map_grid = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    elif level == 3:
        map_grid = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    return map_grid


CELL_SIZE = 200

def main(level):
    grid = create_map(level)
    height = len(grid)
    width = len(grid[0])
    screen_height = height * CELL_SIZE
    screen_width = width * CELL_SIZE

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Muistipeli")

    grid = Grid(grid, CELL_SIZE)

    pygame.init()

    grid.all_sprites.draw(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
