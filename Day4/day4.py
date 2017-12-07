import sys
sys.path.append('..')
import argparse
from common import basic_arguments, read_input_file_words
from itertools import groupby

def day_4(phrase, part):
    if part == '2':
        # sort each word of the input list
        phrase = map(lambda x: ' '.join(map(lambda y: ''.join(sorted(y)), 
                                                        x.split(' '))), phrase)
    # group equal words
    groups = ([list(g) for k,g in groupby(sorted(x.split(' ')))] 
                       for x in phrase)
    # filter elements with more than one element (not valid)
    valid = [g for g in groups if len([x for x in g if len(x) == 1]) == len(g)]
    # return if its valid or not
    return len(valid)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Advent of Code 2017: day 3")
        basic_arguments(parser)
        args = parser.parse_args()

        if args.sequence:
            phrase = [args.sequence.replace('-',' ')]
        elif args.filename:
            phrase = read_input_file_words(args.filename)
        else:
            phrase = read_input_file_words('input')

        print("Solution: {0}".format(day_4(phrase, args.part)))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
