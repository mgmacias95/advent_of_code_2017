import sys
sys.path.append('..')
import argparse
from common import basic_arguments, read_input_file_matrix, str_2_imatrix

def iter_jumps(jumps):
    n_jumps, position = 0, 0
    while position < len(jumps):
        jumps[position] += 1
        position += jumps[position] - 1
        n_jumps += 1
    return n_jumps


def day_5(jumps, part):
    return iter_jumps(jumps)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Advent of Code 2017: day 3")
        basic_arguments(parser)
        args = parser.parse_args()

        if args.sequence:
            jumps = str_2_imatrix(args.sequence, plain=True)
        elif args.filename:
            jumps = read_input_file_matrix(args.filename, plain=True)
        else:
            jumps = read_input_file_matrix('input', plain=True)

        print("Solution: {0}".format(day_5(jumps, args.part)))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
