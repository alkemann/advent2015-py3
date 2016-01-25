
class Cookie:

    def __init__(self, cookie=None):
        if cookie:
            self.capacity = cookie.capacity
            self.durability = cookie.durability
            self.flavor = cookie.flavor
            self.texture = cookie.texture
            self.calories = cookie.calories
            self.spoons = cookie.spoons
            self.score = cookie.score
        else:
            self.capacity = 0
            self.durability = 0
            self.flavor = 0
            self.texture = 0
            self.calories = 0
            self.spoons = 0
            self.score = 0

    def add(self, ingredient, amount=1):
        if amount + self.spoons > 100:
            raise Exception("This would result in too many spoons!")

        self.capacity += ingredient.capacity * amount
        self.durability += ingredient.durability * amount
        self.flavor += ingredient.flavor * amount
        self.texture += ingredient.texture * amount
        self.calories += ingredient.calories * amount
        self.spoons += amount
        self.score = self.calc()

    def calc(self):
        return self.capacity * self.durability * self.flavor * self.texture

    def __str__(self):
        return "%d spoons, capacity %d, durability %d, flavor %d, texture %d, calories %d" % (
            self.spoons, self.capacity, self.durability, self.flavor, self.texture, self.calories)
