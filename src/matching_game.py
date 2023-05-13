import pygame
from sprites.apple import Apple
from sprites.balloon import Balloon
from sprites.heart import Heart
from sprites.moon import Moon
from sprites.star import Star
from sprites.tulip import Tulip
from sprites.carrot import Carrot
from sprites.gem import Gem
from sprites.potato import Potato
from sprites.sun import Sun

class Game:
    """ Luokka, joka luo osan muistipelin korttien kuvien spriteistä.
     
      Attributes:
       grid_map: määrittää tason kartan, 
                jonka perusteella kuvia asetetaan tietty määrä tiettyihin kohtiin.
       cell_size: määrittää yksittäisen spriten koon.
    """

    def __init__(self, grid_map, cell_size):
        """ Konstruktori, luo eri spriteille omat ja kaikille spriteille yhteisen sprite-ryhmän.
        
        Args:
        grid_map: määrittää tason kartan ja spritejen paikan.
        cell_size: määrittää spritejen koon.
        """

        self.grid_map = grid_map
        self.cell_size = cell_size
        self.apples = pygame.sprite.Group()
        self.balloons = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.moons = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_images(grid_map)

    def _initialize_images(self, grid_map):
        """ Luo kuvaspritet tiettyihin kohtiin tasoa tasokartan perusteella ja 
            lisää spritet ryhmiin.

        Args:
        grid_map: määrittää spritejen paikat tasolla.
        """
        map_height = len(grid_map)
        map_width = len(grid_map[0])

        for map_y in range(map_height):
            for map_x in range(map_width):
                cell = self.grid_map[map_y][map_x]
                normalized_x = map_x * self.cell_size
                normalized_y = map_y * self.cell_size

                if cell[1] == 1:
                    self.apples.add(Apple(normalized_x, normalized_y))
                elif cell[1] == 2:
                    self.balloons.add(Balloon(normalized_x, normalized_y))
                elif cell[1] == 3:
                    self.hearts.add(Heart(normalized_x, normalized_y))
                elif cell[1] == 4:
                    self.moons.add(Moon(normalized_x, normalized_y))
                elif cell[1] == 5:
                    self.stars.add(Star(normalized_x, normalized_y))

        self.all_sprites.add(self.apples,
                             self.balloons,
                             self.hearts,
                             self.moons,
                             self.stars)

class Game2:
    """ Luokka, joka luo loput muistipelin spriteistä.

    Attributes:
       grid_map: määrittää tason kartan, 
                jonka perusteella kuvia asetetaan tietty määrä tiettyihin kohtiin.
       cell_size: määrittää yksittäisen spriten koon.
    """

    def __init__(self, grid_map, cell_size):
        """ Konstruktori, luo eri spriteille omat ja 
            kaikille spriteille yhteisen sprite-ryhmän.
        
        Args:
        grid_map: määrittää tason kartan ja spritejen paikan.
        cell_size: määrittää spritejen koon.
        """

        self.grid_map = grid_map
        self.cell_size = cell_size
        self.tulips = pygame.sprite.Group()
        self.carrots = pygame.sprite.Group()
        self.gems = pygame.sprite.Group()
        self.potatoes = pygame.sprite.Group()
        self.suns = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_images(grid_map)

    def _initialize_images(self, grid_map):
        """ Luo kuvaspritet tiettyihin kohtiin tasoa tasokartan perusteella ja 
            lisää spritet ryhmiin.

        Args:
        grid_map: määrittää spritejen paikat tasolla.
        """

        map_height = len(grid_map)
        map_width = len(grid_map[0])
        game1 = Game(self.grid_map, self.cell_size)
        sprites1 = game1.all_sprites

        for map_y in range(map_height):
            for map_x in range(map_width):
                cell = self.grid_map[map_y][map_x]
                normalized_x = map_x * self.cell_size
                normalized_y = map_y * self.cell_size

                if cell[1] == 6:
                    self.tulips.add(Tulip(normalized_x, normalized_y))
                elif cell[1] == 7:
                    self.carrots.add(Carrot(normalized_x, normalized_y))
                elif cell[1] == 8:
                    self.gems.add(Gem(normalized_x, normalized_y))
                elif cell[1] == 9:
                    self.potatoes.add(Potato(normalized_x, normalized_y))
                elif cell[1] == 10:
                    self.suns.add(Sun(normalized_x, normalized_y))

        self.all_sprites.add(sprites1,
                             self.tulips,
                             self.carrots,
                             self.gems,
                             self.potatoes,
                             self.suns)
      