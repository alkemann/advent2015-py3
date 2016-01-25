import re


class Ingredient:

    # Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
    pattern = re.compile("(\w+): capacity ([-]{0,1}\d+), durability ([-]{0,1}\d+), flavor ([-]{0,1}\d+), texture ([-]{0,1}\d+), calories ([-]{0,1}\d+)")

    def __init__(self, description):
        self.name = ""
        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0
        self.description = description
        self.set_from_description()

    def set_from_description(self):
        m = self.pattern.findall(self.description)
        self.name = m[0][0]
        self.capacity = int(m[0][1])
        self.durability = int(m[0][2])
        self.flavor = int(m[0][3])
        self.texture = int(m[0][4])
        self.calories = int(m[0][5])

    def __str__(self):
        return "%s: capacity %d, durability %d, flavor %d, texture %d, calories %d" % (self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories)
