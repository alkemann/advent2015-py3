from unittest import TestCase
from one import *


class TestOneSolution(TestCase):
    def test_floor_counter(self):
        # (()) and ()() both result in floor 0.
        self.assertEqual(0, ends_on_floor("(())"))
        self.assertEqual(0, ends_on_floor("()()"))
        # ((( and (()(()( both result in floor 3.
        self.assertEqual(3, ends_on_floor("((("))
        self.assertEqual(3, ends_on_floor("(()(()("))
        # ))((((( also results in floor 3.
        self.assertEqual(3, ends_on_floor("))((((("))
        # ()) and ))( both result in floor -1 (the first basement level).
        self.assertEqual(-1, ends_on_floor("())"))
        self.assertEqual(-1, ends_on_floor("))("))
        # ))) and )())()) both result in floor -3.
        self.assertEqual(-3, ends_on_floor(")())())"))
        self.assertEqual(-3, ends_on_floor(")))"))

    def test_basement_finder(self):
        # ) causes him to enter the basement at character position 1.
        self.assertEqual(1, enters_basement_after_how_many_steps(")"))
        # ()()) causes him to enter the basement at character position 5.
        self.assertEqual(5, enters_basement_after_how_many_steps("()())"))
