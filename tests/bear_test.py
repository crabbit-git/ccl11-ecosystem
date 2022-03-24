import unittest

from src.bear import Bear
from src.fish import Fish

class TestBear(unittest.TestCase):
    def setUp(self):
        self.bear = Bear("Yogi", "grizzly")

    def test_bear_has_name(self):
        self.assertEqual("Yogi", self.bear.name)
    
    def test_bear_species(self):
        self.assertEqual("grizzly", self.bear.species)

    def test_bear_is_fierce(self):
        self.assertEqual("Miaow", self.bear.roar())

    def test_bear_can_eat_fish(self):
        self.bear.chow_down(Fish("Nemo"))
        self.assertEqual(1, len(self.bear.stomach))
    
    def test_bear_diet(self):
        self.bear.chow_down(Fish("Nemo"))
        self.bear.chow_down(Fish("Bob"))
        self.assertEqual(2, self.bear.food_count())
