from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import os
import sys


def raw_data_generation(length, size, query_size):
    """
    This function generates the raw data for search.
    The data set would be a set of strings.
    Strings are of an alphabet of {0, 1, 2}.

    :param length:     The length of each string
    :param size:    The size of the data set.
    :param query_size:  The size of queries set.
    :return:
    """
    path = "data/" + str(length) + "_" + str(size) + "_" + str(query_size)
    os.makedirs(path)
    file_path = path + "/raw.txt"

    with open(file_path, 'a') as file:
        file.write(str(length) + '\n' + str(size) + '\n' + str(query_size) + '\n')
        for _ in range(size + query_size):
            file.write(build_string(length) + '\n')


def build_string(length):
    """
    Build a string of length len, with alphabet of {0, 1, 2}

    :param length: The length
    :return: String
    """
    s = ""
    for _ in range(length):
        s += str(random.randint(0, 2))
    return s


if __name__ == "__main__":
    argv = sys.argv[1:]
    assert len(argv) == 3

    raw_data_generation(int(argv[0]), int(argv[1]), int(argv[2]))
