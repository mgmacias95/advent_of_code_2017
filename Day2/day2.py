import sys
sys.path.append('..')
import argparse
from common import basic_arguments, str_2_imatrix, read_input_file_matrix
from itertools import combinations

def part_1(checksum):
    """
    get min and max value difference from each row of the matrix and sum them all
    """
    return sum(map(lambda x: max(x) - min(x), checksum))

def part_2(checksum):
    """
    Get all possible combinations of numbers in a row and check its divisibility.
    Sum the divisions that are whole numbers.
    """
    def get_divisible_tuple(row):
        return next(filter(lambda x: not x[0] % x[1], row))

    # From each row, get a tuple of the two evently divisible numbers
    wholediv = map(get_divisible_tuple, map(lambda y: list(combinations(sorted(y, 
                                                    reverse=True), 2)), checksum))
    
    return sum(map(lambda x: x[0] // x[1], wholediv))

def day_2(checksum, part):
    return part_1(checksum) if part == '1' else part_2(checksum)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Advent of Code 2017: day 2")
        basic_arguments(parser)
        args = parser.parse_args()

        if args.sequence:
            checksum = str_2_imatrix(args.sequence)
        elif args.filename:
            checksum = read_input_file_matrix(args.filename)
        else:
            checksum = read_input_file_matrix('input')

        print("Solution: {0}".format(day_2(checksum, args.part)))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
