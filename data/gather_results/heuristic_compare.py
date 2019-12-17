import h5py
import sys
import numpy as np
import pandas as pd


def compare_results(csv_path, h5_path):
    """
    Compare two files that contains their searching results.
    Record the percentage of same results for different K.

    :param csv_file:
    :param h5_file:
    :return:
    """
    acc_res = pd.read_csv(csv_path).to_numpy()
    heur_res = get_heuristic_res(h5_path)

    assert acc_res.shape == heur_res.shape

    k = 10
    res = {}
    q_count = acc_res.shape[0]
    while k <= 100000:
        res[k] = 0.0
        for idx in range(q_count):
            res[k] += np.intersect1d(acc_res[idx], heur_res[idx]).shape[0] / k

    return res



def get_heuristic_res(h5_path):
    """
    Return a numpy array contains heuristic search results
    from a h5 file

    :param h5_path:
    :return:
    """
    with h5py.File(h5_path, 'r') as file:
        return file_path[file['refs']['mih0.res']].value



if __name__ == '__main__':
    argv = sys.argv[1:]
    file_path = argv[:2]
    out_path = argv[2]

    result = compare_results(file_path[0], file_path[1])

    pd.DataFrame(result).to_csv(out_path)
