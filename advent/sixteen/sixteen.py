import re

# Sue 459: cats: 0, children: 7, trees: 3
# Sue 460: vizslas: 4, cats: 6, perfumes: 2
# Sue 461: trees: 3, children: 5, cars: 8
# Sue 462: goldfish: 7, vizslas: 7, children: 5
# Sue 463: cars: 5, akitas: 3, goldfish: 5
# Sue 464: vizslas: 0, pomeranians: 5, cars: 0
# Sue 465: goldfish: 4, akitas: 0, cats: 5
pattern = re.compile("Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")


class Sue:
    def __init__(self, description):
        matches = pattern.findall(description)
        self.id = int(matches[0][0])
        self.hints = {}
        for i in range(1, 4):
            x = i * 2 - 1
            self.hints[matches[0][x]] = int(matches[0][x + 1])

    def __str__(self):
        return "%d %s" % (self.id, self.hints)


knowledge = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def who_is_sue(sues):
    potential = []
    for sue in sues:
        has_potential = True
        for type, score in sue.hints.iteritems():
            if type in knowledge and knowledge[type] != score:
                has_potential = False
        if has_potential:
            return sue.id


facts = {
    "exact": {
        "children": 3,
        "samoyeds": 2,
        "akitas": 0,
        "vizslas": 0,
        "cars": 2,
        "perfumes": 1
    },
    "greater than": {
        "goldfish": 5,
        "pomeranians": 3
    },
    "less than": {
        "trees": 3,
        "cats": 7,
    }
}


def who_is_she_really(sues):
    potential = []
    for sue in sues:
        has_potential = True
        for type, score in sue.hints.iteritems():
            if type in facts["exact"] and facts["exact"][type] != score:
                has_potential = False
            if type in facts["greater than"] and score > facts["greater than"][type]:
                has_potential = False
            if type in facts["less than"] and score < facts["less than"][type]:
                has_potential = False

        if has_potential:
            potential.append(sue)

    return potential