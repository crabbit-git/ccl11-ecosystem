import unittest

from src.fish import Fish

class TestFish(unittest.TestCase):
    def setUp(self):
        self.fish_1 = Fish("Nemo")
        self.fish_2 = Fish("Bob")

    def test_fish_has_name(self):
        self.assertEqual("Nemo", self.fish_1.name)
        self.assertEqual("Bob", self.fish_2.name)
