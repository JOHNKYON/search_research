import h5py
import pandas as pd

import sys

if __name__ == '__main__':
    """
    Gather the results from the given path
    and transform them into a csv file.

    The results will be stored in txt files and .h5 files.
    """
    dic_time = {}
    dic_memory = {}

    args = sys.argv[1:]

    mih_path = "recording/r_m_p0.05/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    if len(args) == 1:
        # Args should be like p0.05
        mih_path = mih_path[:-1] + "_" + args[0] + "/"
        # linear_path = linear_path[:-1] + "_" + args[0] + "/"

    for m in range(16, 65):
        size = 1000000
        dic_time[m] = []

        with h5py.File(mih_path + "mih_128_" + str(size) + "_100_m" + str(m) + "_D8.h5", 'r') as mih_file:
            dic_time[m].append(mih_file['mih'][0][7])
            dic_time[m].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

            dic_memory[m].append(mih_file['mih'][0][9] + mih_file['mih'][0][10])

    df_time = pd.DataFrame(dic_time)
    print(df_time.shape)

    df_mem = pd.DataFrame(dic_memory)

    recording_path = "recording/experiments_m_p0.05_D8_"
    if len(args) == 1:
        recording_path += "_m_" + args[0]
    recording_path_time = recording_path + "time.csv"
    recording_path_mem = recording_path + "mem.csv"
    df_time.to_csv(recording_path_time)
    df_mem.to_csv(recording_path_mem)