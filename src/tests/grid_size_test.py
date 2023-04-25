import unittest
from grid import Grid
from draw_grid import create_map 

class TestGrid(unittest.TestCase):
    def setUp(self):
        map1 = create_map(1)
        map2 = create_map(2)
        map3 = create_map(3)
        self.grid1 = Grid(map1, 200)
        self.grid2 = Grid(map2, 200)
        self.grid3 = Grid(map3, 200)

    def test_grid_size1(self):
        self.assertEqual(self.grid1.size, 3)

    def test_grid_size2(self):
        self.assertEqual(self.grid2.size, 4)

    def test_grid_size3(self):
        self.assertEqual(self.grid3.size, 5)