from random import shuffle
import pygame
from grid import Grid, Layer
from matching_game import Game

def create_map(level):
    if level == 1:
        map_grid = [[(0, 1), (0, 2), (0, 3), (0, 4)],
                    [(0, 5), (0, 6), (0, 2), (0, 3)],
                    [(0, 5), (0, 6), (0, 1), (0, 4)]]
    elif level == 2:
        map_grid = [[(0, 8), (0, 6), (0, 4), (0, 2)],
                    [(0, 7), (0, 7), (0, 5), (0, 1)],
                    [(0, 3), (0, 3), (0, 1), (0, 6)],
                    [(0, 8), (0, 4), (0, 5), (0, 2)]]
    elif level == 3:
        map_grid = [[(0, 1), (0, 10), (0, 2), (0, 9)],
                    [(0, 1), (0, 8), (0, 7), (0, 6)],
                    [(0, 6), (0, 4), (0, 7), (0, 3)],
                    [(0, 10), (0, 2), (0, 8), (0, 9)],
                    [(0, 5), (0, 5), (0, 3), (0, 4)]]
    return map_grid


CELL_SIZE = 200

def main(level):
    grid_map = create_map(level)
    shuffle(grid_map)
    for row in grid_map:
        shuffle(row)
    height = len(grid_map)
    width = len(grid_map[0])
    screen_height = height * CELL_SIZE + 20
    screen_width = width * CELL_SIZE

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Muistipeli")

    grid = Grid(grid_map, CELL_SIZE)
    middle = Layer(grid_map, CELL_SIZE)
    game = Game(grid_map, CELL_SIZE)

    pygame.init()

    game.all_sprites.draw(screen)
    middle.all_sprites.draw(screen)
    grid.all_sprites.draw(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for sprite in game.all_sprites:
                    for mid in middle.all_sprites:
                        if mid.rect.collidepoint(mouse_x, mouse_y) and sprite.rect.collidepoint(mouse_x, mouse_y):
                            screen.blit(mid.image, mid.rect)
                            screen.blit(sprite.image, sprite.rect)
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
