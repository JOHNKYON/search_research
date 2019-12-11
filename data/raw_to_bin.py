from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import h5py
import sys


def raw_to_binary(path, encoder):
    """
    Create a binary file based on raw.txt file
    in given path and a given encoding function.

    The binary file would be of hdf5 format and named
    ${len}_${size}_${querySize}.mat.

    The binary file contains following information:

    keys = ['B', 'Q']
    While   B.shape = (${size}, ${len})
            Q.shape = (${querySize}, ${len})


    :param path:    The path to where the raw data is.
    :return:
    """

    file_path = path + "/raw.txt"
    with open(file_path, 'r') as file:
        length = int(file.readline())
        size = int(file.readline())
        query_size = int(file.readline())

        print("length = " + str(length) + "\t size = " + str(size) + "\t query_size = " + str(query_size))
        with h5py.File(path + "/" + str(length) + "_" + str(size) +
                       "_" + str(query_size) +
                       ".mat", 'w') as h5_file:
            h5_file.create_dataset("B", shape=(size, length/2), dtype='uint8')
            h5_file.create_dataset("Q", shape=(query_size, length/2), dtype='uint8')
            for i in range(size):
                h5_file["B"][i] = encoder.encode("base", file.readline()[:-1])
                print(i)
            for i in range(query_size):
                h5_file["Q"][i] = encoder.encode("query", file.readline()[:-1])


class Encoder:
    """
    A class of encoder that contains a map for encoding and provide
    encoding function
    """

    def __init__(self, base_map=None, query_map=None, heuristic = False):
        if heuristic:
            if base_map is None:
                base_map = {"0": 0,
                            "1": 1,
                            "2": 7}
            if query_map is None:
                query_map = {"0": 10,
                             "1": 11,
                             "2": 7}
        else:
            if base_map is None:
                base_map = {"0": 0,
                            "1": 3,
                            "2": 15}
            if query_map is None:
                query_map = {"0": 0,
                             "1": 5,
                             "2": 15}

        self.map = {"base": base_map,
               "query": query_map}

    def encode(self, name , string):
        length = len(string)
        if length % 2 != 0:
            print("Warning! The encoding length would not fill an 8 bit integer!")
        array = []
        a = 0
        for i in range(length):
            a += self.map[name][string[i]]
            if (i & 1) == 0:
                a <<= 4
            else:
                array.append(a)
                a = 0
        return array


if __name__ == '__main__':
    argv = sys.argv[1:]
    assert len(argv) == 1 or len(argv) == 2

    heuristic = False
    if len(argv) == 2:
        if argv[1] == "True":
            heuristic = True

    encoder = Encoder(heuristic=heuristic)
    raw_to_binary(argv[0], encoder)