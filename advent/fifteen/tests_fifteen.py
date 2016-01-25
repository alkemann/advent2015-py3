import unittest

from SolutionFifteen import SolutionFifteen
from Ingredient import Ingredient
from Cookie import Cookie


class TestOneSolution(unittest.TestCase):

    def test_set_from_description(self):
        t = Ingredient("Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8")
        self.assertEqual("Butterscotch", t.name)
        self.assertEqual(-2, t.durability)

        t = Ingredient("Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3")
        self.assertEqual("Cinnamon", t.name)
        self.assertEqual(3, t.durability)

    def test_cookie(self):
        ingredients = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
        ]
        solver = SolutionFifteen(ingredients)
        solver.add_ingredient("Cinnamon", 100)

        self.assertEqual(100, solver.cookie.spoons)
        self.assertEqual(-200, solver.cookie.flavor)
        self.assertEqual(300, solver.cookie.calories)

    def test_case(self):
        ingredients = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
        ]
        solver = SolutionFifteen(ingredients)
        solver.add_ingredient("Cinnamon", 56)
        solver.add_ingredient("Butterscotch", 44)
        self.assertEqual(44*-1 + 56*2, solver.cookie.capacity)
        self.assertEqual(44*-2 + 56*3, solver.cookie.durability)
        self.assertEqual(44*6 + 56*-2 , solver.cookie.flavor)
        self.assertEqual(44*3 + 56*-1, solver.cookie.texture)

        self.assertEqual(62842880, solver.cookie.score)

    def test_auto_bake(self):
        ingredients = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
        ]
        solver = SolutionFifteen(ingredients)
        cookie = solver.bake()
        self.assertEqual(62842880, cookie.score)
