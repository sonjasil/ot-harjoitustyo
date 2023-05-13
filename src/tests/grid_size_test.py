import unittest
from grid import Grid
from run_game import MatchingGame


class TestGrid(unittest.TestCase):
    def setUp(self):
        map1 = MatchingGame(1).grid_map
        map2 = MatchingGame(2).grid_map
        map3 = MatchingGame(3).grid_map
        self.grid1 = Grid(map1, 200)
        self.grid2 = Grid(map2, 200)
        self.grid3 = Grid(map3, 200)

    def test_grid_size1(self):
        self.assertEqual(len(self.grid1.grid_map), 3)

    def test_grid_size2(self):
        self.assertEqual(len(self.grid2.grid_map), 4)

    def test_grid_size3(self):
        self.assertEqual(len(self.grid3.grid_map), 4)
