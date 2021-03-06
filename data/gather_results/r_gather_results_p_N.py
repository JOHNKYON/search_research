import h5py
import pandas as pd

if __name__ == '__main__':
    """
    Gather the results from the given path
    and transform them into a csv file.

    The results will be stored in txt files and .h5 files.
    """
    dic = {}
    p_list = ["uniform", "p0.1", "p0.05", "p0.01", "simulated"]
    length = 128
    N = 1000000
    m = 32
    D = 8

    mih_path = "recording/r_p_N/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    for _N in range(1, 100):
        N = _N * 10000
        dic[N] = []
        for p in p_list:
            with h5py.File(
                    mih_path + "mih_" + str(length) + "_" + str(N) + "_100" + "_m" \
                    + str(m) + "_D" + str(D) + "_" + p + ".h5",
                    'r') as mih_file:
                dic[N].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/r_experiments_p_N"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)