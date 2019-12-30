import h5py
import pandas as pd

if __name__ == '__main__':
    """
    Gather the results from the given path
    and transform them into a csv file.

    The results will be stored in txt files and .h5 files.
    """
    dic = {}
    length = 128
    N = 1000000
    K = 100
    m = 32

    mih_path = "recording/simulated_N/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    for _N in range(100):
        N = (_N + 1) * 10000
        dic[N] = []
        with h5py.File(
                mih_path + "mih_" + str(length) + "_" + str(N) + "_1000" + "_m" \
                + str(m) + ".h5",
                'r') as mih_file:
            dic[N].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/simulated_N"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)

    dic = {}
    length = 128
    N = 1000000
    m = 32

    mih_path = "recording/simulated_K/"

    for _K in range(1000):
        K = (_K + 1) * 100
        dic[K] = []
        with h5py.File(
                mih_path + "mih_" + str(length) + "_" + str(N) + "_1000" + "_m" \
                + str(m) + "_K" + str(K) + ".h5",
                'r') as mih_file:
            dic[K].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/simulated_K"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)

    dic = {}
    length = 128
    N = 1000000
    m = 32

    mih_path = "recording/simulated_D/"

    for _D in range(16):
        D = _D + 1
        dic[D] = []
        with h5py.File(
                mih_path + "mih_" + str(length) + "_" + str(N) + "_100" + "_m" \
                + str(m) + "_D" + str(D) + "_.h5",
                'r') as mih_file:
            dic[D].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/simulated_D"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)
