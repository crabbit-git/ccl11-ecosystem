import unittest

from src.river import River
from src.fish import Fish

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.river = River("Amazon")
        self.river.contents = [Fish("Bob"), Fish("Nemo")]
    
    def test_river_can_contain_fish(self):
        self.assertEqual(2, len(self.river.contents))
    
    def test_river_can_lose_fish(self):
        self.river.lose_fish(self.river.contents[0])
        self.assertEqual(1, len(self.river.contents))
