import sys
sys.path.append('..')
import argparse
from common import basic_arguments, str_2_imatrix, read_input_file_matrix

def day_2(checksum, part):
    # get min and max value difference from each row of the matrix and sum them all
    return sum(map(lambda x: max(x) - min(x), checksum))

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
