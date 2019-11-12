import h5py
import pandas as pd

import sys

if __name__ == '__main__':
    """
    Gather the results from the given path
    and transform them into a csv file.
    
    The results will be stored in txt files and .h5 files.
    """
    dic = {}

    args = sys.argv[1:]

    mih_path = "recording/experiments_dataset_size/"
    linear_path = "scrpts/data/data/128_1000000_100/"

    if len(args) == 1:
        mih_path = mih_path[:-1] + "_" + args[0] + "/"
        linear_path = linear_path[:-1] + "_" + args[0] + "/"

    for i in range(199):
        size = i * 5000 + 5000
        dic[size] = []

        with h5py.File(mih_path + "mih_128_" + str(size) + "_100_m32.h5", 'r') as mih_file:
            dic[size].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

        if i < 10:
            with open(linear_path + str(size) + "_results.txt", 'r') as linear_file:
                dic[size].append(float(linear_file.readline()))
        else:
            dic[size].append(None)
    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/experiments"
    if len(args) == 1:
        recording_path += "_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)