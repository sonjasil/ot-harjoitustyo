import unittest
from app.grid import Grid
from app.draw_grid import create_map 

class TestGrid(unittest.TestCase):
    def setUp(self):
        map = create_map(1)
        self.grid = Grid(map, 200)

    def test_grid_size(self):
        self.assertEqual(self.grid.size, 3)