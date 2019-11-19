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

    mih_path = "recording/experiments_m/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    if len(args) == 1:
        # Args should be like p0.05
        mih_path = mih_path[:-1] + "_" + args[0] + "/"
        # linear_path = linear_path[:-1] + "_" + args[0] + "/"

    for m in range(18, 65):
        size = 1000000
        dic[m] = []

        with h5py.File(mih_path + "mih_128_" + str(size) + "_100_m" + str(m) + ".h5", 'r') as mih_file:
            dic[m].append(mih_file['mih'][0][7])
            dic[m].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/experiments"
    if len(args) == 1:
        recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)