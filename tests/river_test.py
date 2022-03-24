import unittest

from src.river import River
from src.fish import Fish
from src.bear import Bear

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.river = River("Amazon")
        self.river.contents = [Fish("Bob"), Fish("Nemo"), Fish("Abraham")]
    
    def test_river_has_name(self):
        self.assertEqual("Amazon", self.river.name)
    
    def test_river_population(self):
        self.assertEqual(3, self.river.fish_count())
    
    def test_fish_can_escape(self):
        adventurous_fish = self.river.contents[1]
        self.river.lose_fish(adventurous_fish)
        self.assertEqual(2, len(self.river.contents))

    def test_bear_can_eat_fish(self):
        bear = Bear("Rupert", "brown")
        unlucky_fish = self.river.contents[1]
        bear.chow_down(self.river.lose_fish(unlucky_fish))
        self.assertEqual(2, len(self.river.contents))
        self.assertEqual(1, len(bear.stomach))
    
    def test_bear_is_killing_machine(self):
        bear = Bear("Kuma", "sun")
        buffet = self.river.contents
        doom_clock = len(buffet) - 1
        while len(buffet) != 0:
            bear.chow_down(self.river.lose_fish(buffet[doom_clock]))
            doom_clock -= 1
        self.assertEqual(0, self.river.fish_count())
        self.assertEqual(3, bear.food_count())
