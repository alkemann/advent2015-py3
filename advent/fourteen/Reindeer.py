import re


class Reindeer:

    # "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."
    pattern = re.compile("(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")

    def __init__(self, description):
        self.flying = True
        self.name = "Reindeer"
        self.speed = 0
        self.stamina = 0
        self.rest = 0
        self.description = description
        self.set_values_from_description()
        self.stamina_left = self.stamina
        self.rest_left = 0 #self.rest
        self.distance = 0
        self.score = 0

    def set_values_from_description(self):
        matches = self.pattern.findall(self.description)
        self.name = matches[0][0]
        self.speed = int(matches[0][1])
        self.stamina = int(matches[0][2])
        self.rest = int(matches[0][3])

    def __str__(self):
        return "%s can fly %d km/s for %d seconds, but then must rest for %d seconds." % (self.name, self.speed, self.stamina, self.rest)

    def second(self):
        if self.flying:
            self.distance += self.speed
            self.stamina_left -= 1
            if self.stamina_left == 0:
                self.flying = False
                self.rest_left = self.rest
        else:
            self.rest_left -= 1
            if self.rest_left == 0:
                self.flying = True
                self.stamina_left = self.stamina




