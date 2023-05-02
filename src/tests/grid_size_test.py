import unittest
from grid import Grid
from run_game import MatchingGame 

class TestGrid(unittest.TestCase):
    def setUp(self):
        map1 = MatchingGame(1).create_map(1)
        map2 = MatchingGame(2).create_map(2)
        map3 = MatchingGame(3).create_map(3)
        self.grid1 = Grid(map1, 200)
        self.grid2 = Grid(map2, 200)
        self.grid3 = Grid(map3, 200)

    def test_grid_size1(self):
        self.assertEqual(len(self.grid1.grid_map), 3)

    def test_grid_size2(self):
        self.assertEqual(len(self.grid2.grid_map), 4)

    def test_grid_size3(self):
        self.assertEqual(len(self.grid3.grid_map), 4)