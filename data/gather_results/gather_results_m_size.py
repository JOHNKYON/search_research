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

    p=0.05

    mih_path = "recording/experiments_time_m_len/"
    # linear_path = "scrpts/data/data/128_1000000_100/"

    for m in range(48):
        dic[m+16] = []
        size = 50000
        while size <= 1000000:
            with h5py.File(
                    mih_path + "mih_" + str(length) + "_" + str(size) + "_100" + "_m" + str(m+16) + ".h5",
                    'r') as mih_file:
                dic[m+16].append(mih_file['mih'][0][7] + mih_file['mih'][0][8])
            size += 50000

    df = pd.DataFrame(dic)
    print(df.shape)

    recording_path = "recording/experiments_m_size_p0.05"
    # if len(args) == 1:
    #     recording_path +=  "_m_" + args[0]
    recording_path += ".csv"
    df.to_csv(recording_path)