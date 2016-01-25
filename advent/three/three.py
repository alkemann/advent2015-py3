

def how_many_houses(route):
    x = 0; y = 0; houses = {"%d,%d" % (x, y): 1}
    for c in route:
        if c == '^':
            y += 1
        elif c == '>':
            x += 1
        elif c == 'v':
            y -= 1
        elif c == '<':
            x -= 1

        address = "%d,%d" % (x, y)
        if address not in houses:
            houses[address] = 1

    return len(houses)


def how_many_houses_with_robot(route):
    x = 0; y = 0; xr = 0; yr = 0
    robot = False; houses = {"%d,%d" % (x, y): 1}
    for c in route:
        if c == '^':
            if robot: yr += 1
            else: y += 1
        elif c == '>':
            if robot: xr += 1
            else: x += 1
        elif c == 'v':
            if robot: yr -= 1
            else: y -= 1
        elif c == '<':
            if robot: xr -= 1
            else: x -= 1

        if robot: address = "%d,%d" % (xr, yr)
        else: address = "%d,%d" % (x, y)

        if address not in houses:
            houses[address] = 1

        robot = not robot

    return len(houses)
