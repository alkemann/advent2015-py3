from unittest import TestCase
from three import *


class TestTravel(TestCase):
    def test_how_many_houses(self):
        self.assertEqual(2, how_many_houses(">"))
        self.assertEqual(4, how_many_houses("^>v<"))
        self.assertEqual(2, how_many_houses("^v^v^v^v^v"))

    def test_how_many_robot_houses(self):
        self.assertEqual(3, how_many_houses_with_robot("^v"))
        self.assertEqual(3, how_many_houses_with_robot("^>v<"))
        self.assertEqual(11, how_many_houses_with_robot("^v^v^v^v^v"))
