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
    clicks = 0
    cooldown = 3000
    last = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if clicks == 0:
                    for sprite in game.all_sprites:
                        for mid in middle.all_sprites:
                            for back in grid.all_sprites:
                                if mid.rect.collidepoint(mouse_x, mouse_y) and sprite.rect.collidepoint(mid.rect.x, mid.rect.y):
                                    if sprite.rect.collidepoint(back.rect.x, back.rect.y):
                                        screen.blit(mid.image, mid.rect)
                                        screen.blit(sprite.image, sprite.rect)
                                        sprite1 = sprite
                                        middle_card1 = mid
                                        back1 = back
                                        clicks += 1
                elif clicks == 1:
                    for sprite in game.all_sprites:
                        for mid in middle.all_sprites:
                            for back in grid.all_sprites:
                                if mid.rect.collidepoint(mouse_x, mouse_y) and sprite.rect.collidepoint(mid.rect.x, mid.rect.y):
                                    if sprite.rect.collidepoint(back.rect.x, back.rect.y):
                                        screen.blit(mid.image, mid.rect)
                                        screen.blit(sprite.image, sprite.rect)
                                        sprite2 = sprite
                                        middle_card2 = mid
                                        clicks += 1
                                        back2 = back
            if clicks == 2:    
                now = pygame.time.get_ticks()
                if sprite1.id != sprite2.id and now - last >= cooldown:
                    last = now
                    screen.blit(middle_card1.image, middle_card1.rect)
                    screen.blit(middle_card2.image, middle_card2.rect)
                    screen.blit(back1.image, back1.rect)
                    screen.blit(back2.image, back2.rect)
                    clicks = 0
                elif sprite1.id == sprite2.id and now - last >= cooldown:
                    last = now
                    screen.blit(middle_card1.image, middle_card1.rect)
                    screen.blit(middle_card2.image, middle_card2.rect)
                    sprite1.kill()
                    sprite2.kill()
                    back1.kill()
                    back2.kill()
                    clicks = 0
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
