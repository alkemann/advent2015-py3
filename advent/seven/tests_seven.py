from unittest import TestCase
from seven import *


class TestSix(TestCase):

    def test_set(self):
        strings = ["x -> y", "9 -> x"]
        solver = Seven(strings)
        self.assertEqual(9, solver.check("x"))
        self.assertEqual(9, solver.check("y"))

    def test_not(self):
        strings = ["NOT x -> y", "65530 -> x"]
        solver = Seven(strings)
        self.assertEqual(65530, solver.check("x"))
        self.assertEqual(5, solver.check("y"))

    def test_it(self):
        strings = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i"
        ]
        solver = Seven(strings)
        self.assertEqual(123, solver.check("x"))
        self.assertEqual(72, solver.check("d"))
        self.assertEqual(507, solver.check("e"))
        self.assertEqual(492, solver.check("f"))
        self.assertEqual(114, solver.check("g"))
        self.assertEqual(65412, solver.check("h"))
        self.assertEqual(65079, solver.check("i"))
        self.assertEqual(456, solver.check("y"))