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
    N = 100000
    K = 1000

    mih_path = "recording/entropy_K/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    for _m in range(8):
        m = (_m + 28) * 16
        dic[m] = []
        with h5py.File(
                mih_path + "mih_" + str(length) + "_" + str(N) + "_1000" + "_m" \
                + str(m) + "_K100_simulated.h5",
                'r') as mih_file:
            dic[m].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])
            dic[m].append(mih_file['mih'][0][9] + mih_file['mih'][0][10])

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/simulated_m2"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)
