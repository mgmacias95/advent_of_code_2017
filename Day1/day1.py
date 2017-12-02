import sys
sys.path.append('..')
from common import read_input_file_integers, str_2_ilist
from operator import itemgetter
from itertools import chain
import argparse

parser = argparse.ArgumentParser(description="Advent of Code 2017: day 1")
parser.add_argument('-f', '--file', dest='filename', type=str, help="Input sequence from file")
parser.add_argument('-s', '--sequence', dest='sequence', type=str, help='Input sequence from console')
parser.add_argument('-p', '--part', dest='part', choices=['1','2'], type=str, required=True, help="Part of the problem to solve")

def part_1(captcha):
    """
    [1,2,3,4] -> [(1,2),(2,3),(3,4),(4,1)]
    """
    return zip(captcha,(captcha*2)[1:len(captcha)+1])
    
def part_2(captcha):
    """
    [1,2,3,4] -> [(1,3), (2,4), (3,1), (4,2)]
    """
    midlen = len(captcha) // 2
    return chain.from_iterable((zip(captcha[:midlen], captcha[midlen:]),
                                zip(captcha[midlen:], captcha[:midlen])))

def day_1(captcha, part='1'):
    next_element_tuples = part_1(captcha) if part == '1' else part_2(captcha)
    # filter the ones that are equal
    equal_elements = filter(lambda x: x[0] == x[1], next_element_tuples)
    # sum the 1st element from each tuple
    solution = sum(map(itemgetter(1), equal_elements))
    return solution

if __name__ == '__main__':
    try:
        args = parser.parse_args()

        if args.sequence:
            captcha = str_2_ilist(args.sequence)
        elif args.filename:
            captcha = read_input_file_integers(args.filename)
        else:
            captcha = read_input_file_integers('input')

        print("Solution: {0}".format(day_1(captcha, args.part)))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
