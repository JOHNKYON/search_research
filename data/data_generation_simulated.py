from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import os
import sys
import pandas as pd


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


def build_string_ps(ps):
    """
    This function works similar to build_string

    It build a string with length ${length},

    For each character, it obeys the following rules:
        1 with possibility of 2p.
        2 with possibility of p^2.
        Otherwise 0.
    :param length:
    :param p:
    :return:
    """
    s = ""
    length = len(ps)
    ps = ps.to_numpy()
    for p in ps:
        p = float(p)
        r = random.uniform(0, 1)
        if 0.0 < r < pow(p, 2):
            s += "2"
        elif 1.0 - pow((1.0-p), 2) < r < 1.0:
            s += "0"
        else:
            s += "1"
    return s



def raw_data_generation_r(size, query_size, ps):
    """
    This function functions similarly to raw_data_generation()
    Generate data with given possibilities ps.

    1 is generated with possibility 2p.
    2 is generated with possibility p^2.
    Otherwise 0.
    :return:
    """
    length = len(ps)
    path = "data/" + str(length) + "_" + str(size) + "_" + str(query_size) + "_simulated"
    os.makedirs(path)
    file_path = path + "/raw.txt"
    with open(file_path, 'a') as file:
        file.write(str(length) + '\n' + str(size) + '\n' + str(query_size) + '\n')
        for _ in range(size + query_size):
            file.write(build_string_ps(ps) + '\n')


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


def read_frequencies(length):
    # TODO: Implement
    jsnp_allele_freq = pd.read_csv("data/jsnp_allele_freq.csv")
    jsnp_allele_freq = jsnp_allele_freq[['allele-2 frequency']]

    if length != -1:
        return jsnp_allele_freq[:length]

    return jsnp_allele_freq

if __name__ == "__main__":
    argv = sys.argv[1:]

    assert len(argv) == 2 or len(argv) == 3

    length = -1
    if len(argv) == 3:
        length = int(argv[2])
    ps = read_frequencies(length)
    raw_data_generation_r(int(argv[0]), int(argv[1]), ps)


