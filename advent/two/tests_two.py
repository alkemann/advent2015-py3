from unittest import TestCase
from two import *


class TestSolutionTwo(TestCase):

    # A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52
    # square feet of wrapping paper plus 6 square feet of slack, for a
    # total of 58 square feet.
    def test_how_much_paper_one(self):
        expected = 58
        result = how_much_paper_on_present("2x3x4")
        self.assertEqual(expected, result)

    # A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42
    # square feet of wrapping paper plus 1 square foot of slack, for a
    # total of 43 square feet.
    def test_how_much_paper_two(self):
        expected = 43
        result = how_much_paper_on_present("1x1x10")
        self.assertEqual(expected, result)

    def test_how_much_paper_in_bag(self):
        expected = 43 + 58
        result = how_much_paper_in_bag(["2x3x4", "1x1x10"])
        self.assertEqual(expected, result)

    def test_how_much_ribbon(self):
        expected = 34
        result = how_much_ribbon_for_present("2x3x4")
        self.assertEqual(expected, result)

        expected = 14
        result = how_much_ribbon_for_present("1x1x10")
        self.assertEqual(expected, result)

    def test_how_much_ribbon_in_bag(self):
        expected = 34 + 14
        result = how_much_ribbon_in_bag(["2x3x4", "1x1x10"])
        self.assertEqual(expected, result)
