import sys
sys.path.append('..')
import argparse
from common import basic_arguments
from itertools import combinations

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

def reproduce_square_level(number):
    """
    Given a number, compute its whole square level
    """
    max_elem, level = compute_square(number, 1, 1)
    if level == 0:
        level_items = range(1,2)
    else:
        level_items = range((max_elem - level*8) + 1, max_elem+1)

    return list(level_items)

def day_3(square_grid, part):
    pass

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
