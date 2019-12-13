import math
import numpy as np
import pandas as pd
import os

def cal_arrange(entropies, m):
    """
    Calculate the indices of arrangement that
    maximize the minimum entropy of every substring.

    indices[i] = j
    means that the j-th element in the original array should
    be put at the i-th place in the new array.

    >>> cal_arrange([10,9,8,3,2,1], 3)
    [0, 5, 1, 4, 2, 3]

    :param entropies:
    :param m:
    :return:
    """
    idxes = reversed(np.argsort(entropies).tolist())
    sets = []
    sums = []
    for _ in range(int(m)):
        sets.append([])
        sums.append(0)

    set_order_ptr = 0   # Records if m sets are all filled in one round
    set_order = np.argsort(sums)
    for idx in idxes:
        if set_order_ptr == m:
            set_order_ptr = 0
            set_order = np.argsort(sums)


        # Append the next largest element into the smallest set by far
        sets[set_order[set_order_ptr]].append(idx)
        sums[set_order[set_order_ptr]] += entropies[idx]

        set_order_ptr += 1



    indices = [ele for subset in sets for ele in subset]
    return indices


def cal_entropies(probs):
    """
    Calculates the entropies of every element.

    :param probs:
    :return:
    """
    entropies = []
    for prob in probs:
        entropies.append(cal_entropy(prob[0]))
    return entropies

def cal_entropy(p):
    """
    Calculates the entropy of one element position with a given p.

    :param p:
    :return:
    """
    assert 0 <= p <= 1
    ps = [p ** 2, p * 2, (1 - p) ** 2]

    e = 0.0
    for _p in ps:
        e = e - _p * math.log2(_p)

    return e


def arrange(indices, s):
    """
    This function re-construct string s with a given indices.

    >>> arrange([0, 5, 1, 4, 2, 3], "987321")
    '918273'

    :param indices:
    :param s:
    :return:
    """
    length = len(indices)
    assert len(indices) == len(s)
    res = ""
    for i in range(length):
        res += s[indices[i]]
    return res + "\n"


def get_ps():
    """
    Get probabilities from a fixed given file.

    :return:
    """
    jsnp_allele_freq = pd.read_csv("data/jsnp_allele_freq.csv")
    jsnp_allele_freq = jsnp_allele_freq[['allele-2 frequency']]

    return jsnp_allele_freq.to_numpy()


if __name__ == '__main__':
    l = 4
    m = 84716 / l
    path = "data/84716_100000_1000_simulated/"
    # path = "data/84716_10_5_simulated/"
    raw_path = path + "raw.txt"
    target_path = "data/84716_100000_1000_simulated_arranged"

    os.mkdir(target_path)

    probs = get_ps()
    entropies = cal_entropies(probs)

    indices = cal_arrange(entropies, m)
    count = 0

    with open(raw_path, 'r') as raw_file, open(target_path + "/raw.txt", 'w') as target_file:
        for line in raw_file:
            if count < 3:
                # Write length, data size, query_size
                target_file.write(line)
                count += 1
            else:
                target_file.write(arrange(indices, line[:-1]))





