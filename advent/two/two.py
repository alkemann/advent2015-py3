

# description : string : description of present
# returns : number : square feet of wrapping paper
def how_much_paper_on_present(description):
    sizes = description.split('x')

    length = int(sizes[0])
    width = int(sizes[1])
    height = int(sizes[2])

    sides = [length*width, width*height, height*length]
    sides.sort()
    smallest = sides[0]

    return (2*length*width) + (2*width*height) + (2*height*length) + smallest

def how_much_paper_in_bag(presents):
    total = 0

    for present in presents:
        total += how_much_paper_on_present(present)

    return total

def how_much_ribbon_for_present(description):
    sizes = description.split('x')
    length = int(sizes[0])
    width = int(sizes[1])
    height = int(sizes[2])
    sides = [length, height, width]
    sides.sort()
    return sides[0] * 2 + sides[1] * 2 + length*height*width

def how_much_ribbon_in_bag(presents):
    total = 0

    for present in presents:
        total += how_much_ribbon_for_present(present)

    return total

