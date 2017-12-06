import sys
sys.path.append('..')
import argparse
from common import basic_arguments
from operator import itemgetter

############################ functions for part 1 #############################################
def compute_square(number, square, grid):
    """
    Thinking in the spiral as a recursive geometrical square lead us to the following function.

    The natural numbers are divided in recursive squares:

    s_0 -> 1 (size 1)
    s_1 -> 2 3 4 5 6 7 8 9 (size 8)
    s_2 -> 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 (size 16)
    s_3 -> elements from 25+1 to 25+16 (size 32)

    and so on..

    With this function, the maximum number of each square division is calculated. Using
    this number, we'll be able to reproduce the whole square level.
    """
    if number <= square:
        return (square, grid-1)
    else:
        return compute_square(number, 8*grid + square, grid+1)

def positions(level):
    """
    Returns the relative positions from the center of the square
    """
    positions = list(range(level)) + [level] + list(range(level-1,-1,-1)) 
    positions = positions[:-1] + positions[::-1]
    positions = positions + positions[1:-1]
    return positions[-level+1:] + positions[:-level+1]


def compute_mahattan_distance(number):
    """
    Given a number, compute its manhattan distance:

        1. get the level of the number
        2. get the relative position from the center of each element
        3. if the number is a corner, the distance will be level+1
           otherwise, it will be level
    """
    max_elem, level = compute_square(number, 1, 1)
    level_positions = positions(level)

    if level == 0:
        return 0
    else:
        level_items = range((max_elem - level*8) + 1, max_elem+1)
        return level + level_positions[level_items.index(number)]


############################ functions for part 2 #############################################
def compute_next_coordinate(coords, level, direction):
    """
    Given a coordinates, compute the following ones in the spiral.

    There are 4 possible directions:
        - turn to the left  -> if the values of the coordinates are equal and positive
        - turn down         -> if the abs values of the coordinates are equal. Column is negative
        - turn to the right -> if the values of the coordinates are equal and negative
        - turn up           -> if the abs values of the coordinates are equal. Column is positive
    """
    x, y = coords
    if x == y:
        if x > 0 and y > 0:
            direction = 'left'
        elif x <= 0 and y <= 0:
            direction = 'right'
    elif abs(x) == abs(y):
        if y > 0:
            direction = 'right'
        elif y < 0:
            direction = 'down'
    elif direction == 'right' and y == level:
        direction = 'up' # transition to a new square level

    if direction == 'left':
        next_x = x
        next_y = y-1
    elif direction == 'right':
        next_x = x
        next_y = y+1
    elif direction == 'up':
        next_x = x+1
        next_y = y
    elif direction == 'down':
        next_x = x-1
        next_y = y
    else:
        raise Exception('Unknown direction')

    return (next_x, next_y, direction)


def build_sum_adjacent_spiral(stopper):
    """
    Build an spiral where each element is the sum of its adjacent non-empty elements, diagonal included

    Each element of the spiral has the following information:
        - A tuple which represents its coordinates
        - Its value
        - Its level
    """
    level = 1
    spiral = [((0,0), 1, 0)]
    index = 0
    direction = ''
    while spiral[index][1] <= stopper:
        x, y, direction = compute_next_coordinate(spiral[index][0], level, direction)
        # filter adjacent elements
        adjacent_elements = filter(lambda coords: abs(x - coords[0][0]) < 2 and
                                                  abs(y - coords[0][1]) < 2,
                                    spiral[-8*level:])
        # sum its values
        spiral.append(((x, y), sum(map(itemgetter(1), adjacent_elements)), level))
        index += 1
        if len(list(filter(lambda elem: elem[2] == level, spiral))) == 8*level:
            level += 1

    return spiral[-1][1]


def day_3(square_grid, part):
    return compute_mahattan_distance(square_grid) if part=='1' else \
           build_sum_adjacent_spiral(square_grid)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Advent of Code 2017: day 3")
        basic_arguments(parser)
        args = parser.parse_args()

        if args.sequence:
            square_grid = int(args.sequence)
        elif args.filename:
            raise Exception("File argument disabled for day 3")
        else:
            square_grid = 312051

        print("Solution: {0}".format(day_3(square_grid, args.part)))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
