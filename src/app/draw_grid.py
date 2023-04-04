from app.grid import Grid
import pygame

def create_map(x):
    if x == 1:
        GRID_MAP = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    elif x == 2:
        GRID_MAP = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    elif x == 3:
        GRID_MAP = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    return GRID_MAP


CELL_SIZE = 200

def main(x):
    GRID_MAP = create_map(x)
    height = len(GRID_MAP)
    width = len(GRID_MAP[0])
    screen_height = height * CELL_SIZE 
    screen_width = width * CELL_SIZE 

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Muistipeli")

    grid = Grid(GRID_MAP, CELL_SIZE)

    pygame.init()

    grid.all_sprites.draw(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main(3)