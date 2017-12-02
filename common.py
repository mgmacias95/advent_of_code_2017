def str_2_ilist(str_list):
    """
    '1234' -> [1,2,3,4]
    """
    return list(map(int, str_list))


def read_input_file_integers(filepath):
    """
    Read a sequence of integers from file filepath and stores them in a list
    """
    with open(filepath) as f:
        data = f.read()

    return str_2_ilist(data.strip())
