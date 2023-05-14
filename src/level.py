from random import shuffle


class LevelMap:
    """ Luokka, joka luo tason kartan.

    Attributes:
        level: tason numero, määrittää minkä pohjan mukaan kartta luodaan.
    """

    def __init__(self, level):
        self.level = level
        self.grid_map = self.create_map(self.level)
        self.cell_size = 200
        self.screen_height = None
        self.screen_width = None

        self.create_map(self.level)

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
        self.screen_height = height * self.cell_size + 80
        self.screen_width = width * self.cell_size
