import h5py
import sys
import numpy as np
import pandas as pd


def compare_reults(csv_file, h5_file):
    """
    Compare two files that contains their searching results.
    Record the percentage of same results for different K.

    :param csv_file:
    :param h5_file:
    :return:
    """
    pass

if __name__ == '__main__':
    argv = sys.argv[1:]
    file_path = argv[:2]
    out_path = argv[2]

    result = compare_retuls(file_path[0], file_path[1])

