import unittest

from src.bear import Bear

class TestBear(unittest.TestCase):
    def setUp(self):
        self.bear = Bear("Yogi", "grizzly")

    def test_bear_has_name(self):
        self.assertEqual("Yogi", self.bear.name)