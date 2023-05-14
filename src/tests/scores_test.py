import unittest
from run_game import MatchingGame


class TestScores(unittest.TestCase):
    def setUp(self):
        self.game = MatchingGame(1)

    def test_correct_highscore(self):
        self.game.scores = [12, 11, 14]
        highscore = self.game.get_highscore()

        self.assertEqual(highscore, 11)

    def test_empty_highscore(self):
        self.game.scores = []
        highscore = self.game.get_highscore()

        self.assertEqual(highscore, "-")

    def test_do_not_load_low_score(self):
        self.game.scores = []
        self.game.score = 5
        self.game.load_scores()

        self.assertEqual(self.game.scores, [])

    def test_load_score_level1(self):
        self.game.scores = []
        self.game.score = 7
        self.game.load_scores()

        self.assertEqual(self.game.scores, [7])

    def test_load_score_level2(self):
        self.game = MatchingGame(2)
        self.game.scores = []
        self.game.score = 10
        self.game.load_scores()

        self.assertEqual(self.game.scores, [10])

    def test_load_score_level3(self):
        self.game = MatchingGame(3)
        self.game.scores = []
        self.game.score = 12
        self.game.load_scores()

        self.assertEqual(self.game.scores, [12])