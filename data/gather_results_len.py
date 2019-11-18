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
    m = 64

    p=0.1

    mih_path = "recording/experiments_len/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    length = 128
    while length <= 448:
        size = 500000
        dic[length] = []

        with h5py.File(mih_path + "mih_" + str(length) + "_" + str(size) + "_100_p" +str(p) + "_m" + str(m) + ".h5", 'r') as mih_file:
            dic[length].append(mih_file['mih'][0][7])
            dic[length].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])
        length += 64

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/experiments_m64_len"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)