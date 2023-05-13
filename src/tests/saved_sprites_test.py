import unittest
from run_game import MatchingGame

class TestSpriteId(unittest.TestCase):
    def setUp(self):
        self.game = MatchingGame(1)
        self.sprite1 = self.game.sprite1
        self.sprite2 = self.game.sprite2

    def test_sprite1_exists(self):
        self.game.click_1()
        
        self.assertIsNotNone(self.sprite1)

    def test_sprite2_exists(self):
        self.game.click_1()
        self.game.click_2()

        self.assertIsNotNone(self.sprite2)
