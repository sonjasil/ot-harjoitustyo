import pygame
from sprites.back import Back
from sprites.middle import Middle

class Grid:
    """ Luokka, joka luo ruudukon muistipelin korttien takaosista.

    Attributes:
       grid_map: määrittää tason kartan, jonka perusteella kuvia asetetaan tietty määrä tiettyihin kohtiin.
       cell_size: määrittää yksittäisen spriten koon.
    """

    def __init__(self, grid_map, cell_size):
        """ Konstruktori, joka luo spriteille ryhmät.

        Args:
        grid_map: määrittää tason kartan ja spritejen paikan.
        cell_size: määrittää spritejen koon.
        
        """

        self.grid_map = grid_map
        self.cell_size = cell_size
        self.size = len(grid_map)
        self.backs = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(grid_map)

    def _initialize_sprites(self, grid_map):
        """ Luo spritet tiettyihin kohtiin tason kartan mukaan. Takaspritet luodaan jokaiseen kartan kohtaan.
        
        Args:
        grid_map: määrittää spritejen kohdat tasolla.

        """

        height = len(grid_map)
        width = len(grid_map[0])

        for grid_y in range(height):
            for grid_x in range(width):
                cell = self.grid_map[grid_y][grid_x]
                normalized_x = grid_x * self.cell_size
                normalized_y = grid_y * self.cell_size

                if cell[0] == 0:
                    self.backs.add(Back(normalized_x, normalized_y))

            self.all_sprites.add(self.backs)

class Layer:
    """ Luokka, spriteistä tyhjän kerroksen korttien kuvien ja takaosien väliin.

    Attributes:
       grid_map: määrittää tason kartan, jonka perusteella kuvia asetetaan tietty määrä tiettyihin kohtiin.
       cell_size: määrittää yksittäisen spriten koon.

    """

    def __init__(self, grid_map, cell_size):
        """ Konstruktori, joka luo spriteille ryhmät.

        Args:
        grid_map: määrittää tason kartan ja spritejen paikan.
        cell_size: määrittää spritejen koon.

        """
         
        self.grid_map = grid_map
        self.cell_size = cell_size
        self.size = len(grid_map)
        self.middles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(grid_map)

    def _initialize_sprites(self, grid_map):
        """ Luo spritet tiettyihin kohtiin tason kartan mukaan. Välispritet luodaan tason jokaiseen kohtaan.
        
        Args:
        grid_map: määrittää spritejen kohdat tasolla.
        
        """

        height = len(grid_map)
        width = len(grid_map[0])

        for middle_y in range(height):
            for middle_x in range(width):
                cell = self.grid_map[middle_y][middle_x]
                normalized_x = middle_x * self.cell_size
                normalized_y = middle_y * self.cell_size

                if cell[0] == 0:
                    self.middles.add(Middle(normalized_x, normalized_y))

            self.all_sprites.add(self.middles)
