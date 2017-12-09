import sys
sys.path.append('..')
import argparse
from common import basic_arguments, read_input_file_matrix, str_2_imatrix
import hashlib

def day_6(banks, part):
    found_configurations = set()
    last_config = banks
    last_hash = hashlib.md5(str(last_config).encode()).hexdigest()
    iterations = 0
    while last_hash not in found_configurations:
        found_configurations.add(last_hash)
        # get the maximum numbers of blocks and the bank they belong to
        max_blocks = max(last_config)
        index = last_config.index(max_blocks)
        last_config[index] = 0
        
        for i in range(max_blocks):
            index = (index+1)%len(last_config)
            last_config[index] += 1

        iterations += 1
        last_hash = hashlib.md5(str(last_config).encode()).hexdigest()
    return iterations

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Advent of Code 2017: day 3")
        basic_arguments(parser)
        args = parser.parse_args()

        if args.sequence:
            banks = str_2_imatrix(args.sequence, plain=True)
        elif args.filename:
            banks = read_input_file_matrix(args.filename, plain=True)
        else:
            banks = read_input_file_matrix('input', plain=True)

        print("Solution: {0}".format(day_6(banks, args.part)))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
