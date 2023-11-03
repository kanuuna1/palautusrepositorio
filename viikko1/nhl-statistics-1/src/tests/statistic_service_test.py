import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    # ...

    def test_search(self):
        #f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"
        s = "Kurri EDM 37 + 53 = 90"
        self.assertEqual(str(self.stats.search("Kurri")), s)
    
    def test_search_none(self):
        self.assertEqual(str(self.stats.search("Selanne")), "None")

    def test_team(self):
        self.assertAlmostEqual(str(self.stats.team("PIT")[0]), str(Player("Lemieux", "PIT", 45, 54)))
    
    def test_top(self):
        #self.assertAlmostEqual(str(self.stats.top(0)), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertAlmostEqual(str(self.stats.top(1)[0]), str(Player("Gretzky", "EDM", 35, 89)))

    