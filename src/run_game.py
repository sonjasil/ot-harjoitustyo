import pickle
import pygame
from grid import Grid, Layer
from matching_game import Game2
from level import LevelMap


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

        self.lvl = level
        self.level = LevelMap(self.lvl)
        self.level.initialize_map()
        self.grid_map = self.level.grid_map
        self.grid = Grid(self.grid_map, self.level.cell_size)
        self.middle = Layer(self.grid_map, self.level.cell_size)
        self.game = Game2(self.grid_map, self.level.cell_size)
        self.last = None
        self.clicks, self.score = 0, 0
        self.scores = self.get_scores()
        self.box = pygame.Rect(0, self.level.screen_height -
                               80, self.level.screen_width, 80)
        self.mouse_x, self.mouse_y = 0, 0

        self.sprite1, self.sprite2 = None, None
        self.middle_card1, self.middle_card2 = None, None
        self.back1, self.back2 = None, None

        self.screen = pygame.display.set_mode(
            (self.level.screen_width, self.level.screen_height))
        pygame.display.set_caption("Muistipeli")

    def run_game(self):
        """Suorittaa peliä, päivittää näyttöä ja seuraa tapahtumia näytöllä
        """

        pygame.init()
        running = True
        self.draw_sprites()
        self.last = pygame.time.get_ticks()

        while running:
            self.render_text()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_x, self.mouse_y = event.pos
                    if self.clicks == 0:
                        self.click_1()
                    elif self.clicks == 1:
                        self.click_2()
                        self.last = pygame.time.get_ticks()
                if self.clicks == 2:
                    self.turn_cards()
                if event.type == pygame.QUIT:
                    self.load_scores()
                    running = False
            pygame.display.flip()
        pygame.quit()

    def draw_sprites(self):
        """Piirtää spritet näytölle kerroksittain.
        """

        self.game.all_sprites.draw(self.screen)
        self.middle.all_sprites.draw(self.screen)
        self.grid.all_sprites.draw(self.screen)

    def render_text(self):
        """Piirtää tekstin ja pistelaskurin näytölle.
        """
        text_font = pygame.font.SysFont("Arial", 24)
        highscore = self.get_highscore()
        text1 = text_font.render(
            f"Käännetyt parit: {self.score}", True, (255, 255, 255))
        text2 = text_font.render(
            f"Paras tulos: {highscore}", True, (255, 255, 255))
        self.screen.blit(text1, (self.level.screen_width // 2 +
                         40, self.level.screen_height - 50))
        self.screen.blit(text2, (20, self.level.screen_height - 50))

    def get_scores(self):
        """Hakee pelaajan kaikki tulokset tiedostosta.

        Returns:
        list(scores): Lista pelaajan kaikista saamista pisteistä.
        tai
        list(): Tyhjä lista, jos tiedostoa ei ole vielä olemassa.
        """

        try:
            if self.lvl == 1:
                file = open("scores.p", "rb")
            elif self.lvl == 2:
                file = open("scores2.p", "rb")
            elif self.lvl == 3:
                file = open("scores3.p", "rb")
            scores = pickle.load(file)
            file.close()
            return list(scores)
        except:
            return list()

    def get_highscore(self):
        """Hakee pelaajan parhaan tuloksen listasta, jos pelaajalla on tuloksia.

        Returns:
        min(self.scores): Pienin arvo pelaajan kaikista hyväksytyistä pisteistä.
        tai
        "-": Pelkkä merkki, jos pelaajalla ei ole vielä tallennettuja pisteitä.
        """

        try:
            return min(self.scores)
        except:
            return "-"

    def load_scores(self):
        """Lataa pelaajan tulokset tason perusteella eri tiedostoihin, jos pisteet ovat vähintään korttiparien määrä.
        """
        if self.lvl == 1 and self.score >= 6:
            self.scores.append(self.score)
        elif self.lvl == 2 and self.score >= 8:
            self.scores.append(self.score)
        elif self.lvl == 3 and self.score >= 10:
            self.scores.append(self.score)

        if self.lvl == 1:
            file = open("scores.p", "wb")
        elif self.lvl == 2:
            file = open("scores2.p", "wb")
        elif self.lvl == 3:
            file = open("scores3.p", "wb")

        pickle.dump(self.scores, file)
        file.close()

    def click_1(self):
        """Piirtää ensimmäisen käännetyn kortin.
        """

        for img in self.game.all_sprites:
            for mid in self.middle.all_sprites:
                for back in self.grid.all_sprites:
                    if mid.rect.collidepoint(self.mouse_x, self.mouse_y
                                             ) and img.rect.collidepoint(mid.rect.x, mid.rect.y
                                                                         ) and img.rect.collidepoint(back.rect.x, back.rect.y):
                        self.screen.blit(mid.image, mid.rect)
                        self.screen.blit(img.image, img.rect)
                        self.sprite1 = img
                        self.middle_card1 = mid
                        self.back1 = back
                        self.clicks += 1

    def click_2(self):
        """Piirtää toisen käännetyn kortin ruudulle. Lisää pistelaskurin summaa.
        """

        pygame.draw.rect(self.screen, (0, 0, 0), self.box)
        for img in self.game.all_sprites:
            for mid in self.middle.all_sprites:
                for back in self.grid.all_sprites:
                    if mid.rect.collidepoint(self.mouse_x, self.mouse_y
                                             ) and img.rect.collidepoint(mid.rect.x, mid.rect.y
                                                                         ) and img.rect.collidepoint(back.rect.x, back.rect.y):
                        self.screen.blit(mid.image, mid.rect)
                        self.screen.blit(img.image, img.rect)
                        self.sprite2 = img
                        self.middle_card2 = mid
                        self.back2 = back
        if self.sprite1.rect != self.sprite2.rect:
            self.clicks += 1
            self.score += 1

    def turn_cards(self):
        """Kääntää käännetyt kortit takaisin ympäri, 
            jos ne eivät ole pari tai poistaa kortit, jos ne ovat pari. 
            Poistaa poistettujen korttien paikat käytöstä.
        """

        now = pygame.time.get_ticks()
        cooldown = 2500
        if self.sprite1.id != self.sprite2.id and now - self.last >= cooldown:
            self.last = now
            self.screen.blit(self.middle_card1.image, self.middle_card1.rect)
            self.screen.blit(self.middle_card2.image, self.middle_card2.rect)
            self.screen.blit(self.back1.image, self.back1.rect)
            self.screen.blit(self.back2.image, self.back2.rect)
            self.clicks = 0
        elif self.sprite1.id == self.sprite2.id and now - self.last >= cooldown:
            self.last = now
            self.screen.blit(self.middle_card1.image, self.middle_card1.rect)
            self.screen.blit(self.middle_card2.image, self.middle_card2.rect)
            self.sprite1.kill()
            self.sprite2.kill()
            self.back1.kill()
            self.back2.kill()
            self.clicks = 0
