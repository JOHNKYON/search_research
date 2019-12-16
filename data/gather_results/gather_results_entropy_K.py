import h5py
import pandas as pd

if __name__ == '__main__':
    """
    Gather the results from the given path
    and transform them into a csv file.

    The results will be stored in txt files and .h5 files.
    """
    dic = {}
    dic_arr = {}
    length = 1024
    m = 512

    mih_path = "recording/entropy_K/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    K = 10
    while K <= 100000:
        size = 100000
        dic[K] = []
        dic_arr[K] = []

        with h5py.File(mih_path + "mih_" + str(length) + "_" + str(size) + "_1000" + "_m" + str(m) \
                       + "_K" + str(K) + "_simulated.h5", 'r') as mih_file:
            dic[K].append(mih_file['mih'][0][7])
            dic[K].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

        with h5py.File(mih_path + "mih_" + str(length) + "_" + str(size) + "_1000" + "_m" + str(m) \
                       + "_K" + str(K) + "_simulated_arranged.h5", 'r') as mih_file:
            dic_arr[K].append(mih_file['mih'][0][7])
            dic_arr[K].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])
        K *= 10

    df = pd.DataFrame(dic)
    df_arr = pd.DataFrame(dic_arr)
    print(df.shape)

    recording_path = "recording/entropy_K"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    df.to_csv(recording_path + "origin.csv")
    df_arr.to_csv(recording_path + "arranged.csv")