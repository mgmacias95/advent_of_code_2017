import sys
sys.path.append('..')
from common import read_input_file_integers, str_2_ilist
from operator import itemgetter
import argparse

parser = argparse.ArgumentParser(description="Advent of Code 2017: day 1")
parser.add_argument('-f', '--file', dest='filename', type=str, help="Input problem from file")
parser.add_argument('-p', '--problem', dest='problem', type=str, help='Input problem from console')

if __name__ == '__main__':
    try:
        args = parser.parse_args()

        if args.problem:
            captcha = str_2_ilist(args.problem)
        elif args.filename:
            captcha = read_input_file_integers(args.filename)
        else:
            captcha = read_input_file_integers('input')

        # [1,2,3,4] -> [(1,2),(2,3),(3,4),(4,1)]
        next_element_tuples = zip(captcha,(captcha*2)[1:len(captcha)+1])
        # filter the ones that are equal
        equal_elements = filter(lambda x: x[0] == x[1], next_element_tuples)
        # sum the 1st element from each tuple
        solution = sum(map(itemgetter(1), equal_elements))

        print("Solution: {0}".format(solution))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
