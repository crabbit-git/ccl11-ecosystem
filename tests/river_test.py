import unittest

from src.river import River
from src.fish import Fish
from src.bear import Bear

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.river = River("Amazon")
        self.river.contents = [Fish("Bob"), Fish("Nemo"), Fish("Abraham")]
    
    def test_river_contains_3_fish(self):
        self.assertEqual(3, self.river.population_check())
    
    def test_river_can_lose_fish(self):
        unlucky_fish = self.river.contents[1]
        self.river.lose_fish(unlucky_fish)
        self.assertEqual(2, len(self.river.contents))

    def test_bear_is_killing_machine(self):
        bear = Bear("Ronald", "polar")
        unlucky_fish = self.river.contents[1]
        bear.chow_down(self.river.lose_fish(unlucky_fish))
        self.assertEqual(2, len(self.river.contents))
        self.assertEqual(1, len(bear.stomach))
