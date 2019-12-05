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

    mih_path = "recording/experiments_len2m/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    if len(args) == 1:
        # Args should be like p0.05
        mih_path = mih_path[:-1] + "_" + args[0] + "/"
        # linear_path = linear_path[:-1] + "_" + args[0] + "/"

    for _l in range(16):
        l = (_l+1) * 64
        m = int(l / 2)
        size = 500000
        dic_time[m] = []
        dic_memory[m] = []

        with h5py.File(mih_path + "mih_" + str(l) + "_" + str(size) + "_100_p0.1_m" + str(m) + ".h5", 'r') as mih_file:
            dic_time[m].append(mih_file['mih'][0][7])
            dic_time[m].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

            dic_memory[m].append(mih_file['mih'][0][9] + mih_file['mih'][0][10])

    df_time = pd.DataFrame(dic_time)
    print(df_time.shape)

    df_mem = pd.DataFrame(dic_memory)

    recording_path = "recording/k_experiments_len2m_p0.1"
    if len(args) == 1:
        recording_path += "_m_" + args[0]
    recording_path_time = recording_path + "time.csv"
    recording_path_mem = recording_path + "mem.csv"
    df_time.to_csv(recording_path_time)
    df_mem.to_csv(recording_path_mem)