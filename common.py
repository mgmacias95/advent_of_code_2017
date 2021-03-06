from itertools import chain

def str_2_ilist(str_list):
    """
    '1234' -> [1,2,3,4]
    """
    return list(map(int, str_list))

def str_2_imatrix(str_matrix, plain):
    """
    '1 2 3 4\n1 2 3\n1 2 3 4'

    ->

    1 2 3 4
    1 2 3
    1 2 3 4
    """
    matrix = list(map(str_2_ilist, map(lambda x: x.split(' '), str_matrix.split('*'))))
    if not plain:
        return matrix
    else:
        return list(chain.from_iterable(matrix))

def read_input_file_integers(filepath):
    """
    Read a sequence of integers from file filepath and stores them in a list
    """
    with open(filepath) as f:
        data = f.read()

    return str_2_ilist(data.strip())

def read_input_file_matrix(filepath, plain=False):
    """
    Read a matrix of integers from file filepath and stores them in a list of lists
    """
    with open(filepath) as f:
        data = f.read()

    return str_2_imatrix(data.replace('\n','*').replace('\t',' ')[:-1], plain) # remove last \n

def read_input_file_words(filepath):
    """
    Read a list of phrases from a file
    """
    with open(filepath) as f:
        data = f.read().split('\n')[:-1]

    return data

def basic_arguments(parser):
    parser.add_argument('-f', '--file', dest='filename', type=str, help="Input sequence from file")
    parser.add_argument('-s', '--sequence', dest='sequence', type=str, help='Input sequence from console')
    parser.add_argument('-p', '--part', dest='part', choices=['1','2'], type=str, required=True, help="Part of the problem to solve")
