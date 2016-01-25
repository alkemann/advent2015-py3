from Ingredient import Ingredient
from Cookie import Cookie


class SolutionFifteen:
    def __init__(self, ingredients):
        self.cookie = Cookie()
        self.ingredients = {}
        for value in ingredients:
            i = Ingredient(value)
            self.ingredients[i.name] = i

    def add_ingredient(self, name, amount):
        ingredient = self.ingredients.get(name)
        self.cookie.add(ingredient, amount)

    def bake(self):
        cookie = Cookie()

        # add one of each ingredient
        for ingredient in self.ingredients.values():
            cookie.add(ingredient)

        rounds = 100 - len(self.ingredients)

        # add the rest of the 100 spoons
        for round in range(0, rounds):
            competitors = []
            # make a new cookie with one more of each ingredient
            for ingredient in self.ingredients.values():
                tmp = Cookie(cookie)  # start with previous state
                tmp.add(ingredient)
                competitors.append(tmp)

            # look through the competitors and grab the one with
            # the best score for next iteration
            best = None
            highest = 0
            for c in competitors:
                if highest < c.score:
                    best = c
                    highest = c.score

            cookie = best

        return cookie
