from random import shuffle
import pygame
from grid import Grid, Layer
from matching_game import Game2

class MatchingGame:
    """ Luokka, joka luo muistipelin tason mukaan.
    
    Attributes: 
        level: Pelin taso, määrittää ruudukon koon.
    """

    def __init__(self, level):
        """Konstruktori, luo pelin ruudukon ja spritet kerroksittain.
        
        Args:
            level: Pelin taso, määrittää ruudukon koon
        """
        
        self.level = level
        self.grid_map = self.create_map(self.level)
        self.CELL_SIZE = 200
        self.grid = Grid(self.grid_map, self.CELL_SIZE)
        self.middle = Layer(self.grid_map, self.CELL_SIZE)
        self.game = Game2(self.grid_map, self.CELL_SIZE)

    def create_map(self, level):
        """Luo pelin ruudukon tason perusteella
        
        Args:
            level: Pelin taso.

        Returns:
            map_grid: Pelin taso taulukkona, jossa tuplejen numerot vastaavat spriteja.
        """

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
            map_grid = [[(0, 1), (0, 10), (0, 2), (0, 9), (0, 5)],
                         [(0, 1), (0, 8), (0, 7), (0, 6), (0, 5)],
                         [(0, 6), (0, 4), (0, 7), (0, 3), (0, 3)],
                         [(0, 10), (0, 2), (0, 8), (0, 9), (0, 4)]]
        return map_grid
    
    def initialize_map(self):
        """Alustaa ruudukon ja näytön koon ruudukon mukaan.
        """

        shuffle(self.grid_map)
        for row in self.grid_map:
            shuffle(row)
        height = len(self.grid_map)
        width = len(self.grid_map[0])
        self.screen_height = height * self.CELL_SIZE + 80
        self.screen_width = width * self.CELL_SIZE

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Muistipeli")

    def run_game(self):
        """Suorittaa peliä, päivittää näyttöä ja seuraa tapahtumia näytöllä
        """

        pygame.init()
        self.initialize_map()
        self.set_elements()
        self.draw_sprites()
        self.last = pygame.time.get_ticks()

        while self.running:
            self.render_text()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_x, self.mouse_y = event.pos
                    if self.clicks == 0:
                         self.click_1()
                    elif self.clicks == 1:
                         self.click_2()
                if self.clicks == 2:
                    self.turn_cards()
                if event.type == pygame.QUIT:
                    self.running = False         
            pygame.display.flip()
        pygame.quit()

    def draw_sprites(self):
        """Piirtää spritet näytölle kerroksittain.
        """

        self.game.all_sprites.draw(self.screen)
        self.middle.all_sprites.draw(self.screen)
        self.grid.all_sprites.draw(self.screen)

    def set_elements(self):
        """Määrittää ohjelman suorituksen muuttujat.
        """

        self.running = True
        self.clicks = 0
        self.score = 0
        self.cooldown = 3000
        self.text_font = pygame.font.SysFont("Arial", 24)
        self.box = pygame.Rect(0, self.screen_height - 80, self.screen_width, 80)

    def render_text(self):
        """Piirtää tekstin ja pistelaskurin näytölle.
        """

        text = self.text_font.render(f"Käännetyt parit: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (self.screen_width // 2 + 40, self.screen_height - 50))

    def click_1(self):
        """Piirtää ensimmäisen käännetyn kortin.
        """

        for sprite in self.game.all_sprites:
            for mid in self.middle.all_sprites:
                for back in self.grid.all_sprites:
                    if mid.rect.collidepoint(self.mouse_x, self.mouse_y) and sprite.rect.collidepoint(mid.rect.x, mid.rect.y):
                        if sprite.rect.collidepoint(back.rect.x, back.rect.y):
                            self.screen.blit(mid.image, mid.rect)
                            self.screen.blit(sprite.image, sprite.rect)
                            self.sprite1 = sprite
                            self.middle_card1 = mid
                            self.back1 = back
                            self.clicks += 1

    def click_2(self):
        """Piirtää toisen käännetyn kortin ruudulle. Lisää pistelaskurin summaa.
        """

        self.score += 1
        pygame.draw.rect(self.screen, (0, 0, 0), self.box)
        for sprite in self.game.all_sprites:
            for mid in self.middle.all_sprites:
                for back in self.grid.all_sprites:
                    if mid.rect.collidepoint(self.mouse_x, self.mouse_y) and sprite.rect.collidepoint(mid.rect.x, mid.rect.y):
                        if sprite.rect.collidepoint(back.rect.x, back.rect.y):
                            self.screen.blit(mid.image, mid.rect)
                            self.screen.blit(sprite.image, sprite.rect)
                            self.sprite2 = sprite
                            self.middle_card2 = mid
                            self.clicks += 1
                            self.back2 = back
    def turn_cards(self):
        """Kääntää käännetyt kortit takaisin ympäri, jos ne eivät ole pari tai poistaa kortit, jos ne ovat pari. Poistaa poistettujen korttien paikat käytöstä.
        """

        now = pygame.time.get_ticks()
        if self.sprite1.id != self.sprite2.id and now - self.last >= self.cooldown:
            self.last = now
            self.screen.blit(self.middle_card1.image, self.middle_card1.rect)
            self.screen.blit(self.middle_card2.image, self.middle_card2.rect)
            self.screen.blit(self.back1.image, self.back1.rect)
            self.screen.blit(self.back2.image, self.back2.rect)
            self.clicks = 0
        elif self.sprite1.id == self.sprite2.id and now - self.last >= self.cooldown:
            self.last = now
            self.screen.blit(self.middle_card1.image, self.middle_card1.rect)
            self.screen.blit(self.middle_card2.image, self.middle_card2.rect)
            self.sprite1.kill()
            self.sprite2.kill()
            self.back1.kill()
            self.back2.kill()
            self.clicks = 0
