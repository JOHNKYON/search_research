import h5py
import pandas as pd

if __name__ == '__main__':
    """
    Gather the results from the given path
    and transform them into a csv file.

    The results will be stored in txt files and .h5 files.
    """
    dic = {}
    length = 1024
    m = 512
    size = 100000
    K = 2000

    mih_path = "recording/heuristic_K"
    # linear_path = "scrpts/data/data/128_1000000_100/"


    dic[K] = []

    with h5py.File(mih_path + "mih_" + str(length) + "_" + str(size) + "_1000" + "_m" + str(m) \
                   + "_K" + str(K) + "_simulated_heuristic.h5", 'r') as mih_file:
        dic[K].append(mih_file['mih'][0][7])
        dic[K].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])
        dic[K].append(mih_file['mih'][0][9] + mih_file['mih'][0][10])

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    df.to_csv(recording_path + "heuristic_time_mem.csv")
