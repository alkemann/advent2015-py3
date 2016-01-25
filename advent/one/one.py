

def ends_on_floor(plan):
    floor = 0
    for c in plan:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            print "ERROR"
    return floor


def enters_basement_after_how_many_steps(plan):
    floor = 0
    step = 0
    for c in plan:
        step += 1
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

        if floor == -1:
            return step
