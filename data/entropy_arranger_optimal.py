import math
import pandas as pd
import os
import sys

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
    sets = []
    sets_temp = []
    sums = []
    sums_temp = []
    for _ in range(int(m)):
        sets.append([])
        sums.append(0)
        sets_temp.append([])
        sums_temp.append(0)

    diff = [1.0e6]
    dp(sets_temp, sums_temp, sets, sums, m, 0, 0, entropies, diff)

    indices = [ele for subset in sets for ele in subset]
    return indices


def dp(sets, sums, s, sm, m, ptr, level, es, diff):
    if ptr == len(es):
        temp = cal_diff(sums)
        if temp < diff[0]:
            copy(sets, s)
            diff[0] = temp
        return

    if diff[0] == 0:
        return

    if ptr % m == 0:
        level += 1

    for i in range(m):
        if len(sets[i]) < level:
            sums[i] += es[ptr]
            sets[i].append(ptr)
            dp(sets, sums, s, sm, m, ptr+1, level, es, diff)
            sums[i] -= es[ptr]
            sets[i] = sets[i][:-1]


def cal_diff(sums):
    max = sums[0]
    min = sums[0]
    for sum in sums:
        max = max if max >= sum else sum
        min = min if min <= sum else sum
    return max - min

def copy(a_sets, b_sets):
    """
    >>> a_sets = [[0,1],[2,3]]
    >>> b_sets = [[], []]
    >>> copy(a_sets, b_sets)
    >>> b_sets
    [[0, 1], [2, 3]]
    >>> a_sets[0][0] = 5
    >>> a_sets
    [[5, 1], [2, 3]]
    >>> b_sets
    [[0, 1], [2, 3]]

    :param a_sets:
    :param b_sets:
    :return:
    """
    for i in range(len(a_sets)):
        b_sets[i] = list(a_sets[i])


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


def get_ps(length):
    """
    Get probabilities from a fixed given file.

    :return:
    """
    jsnp_allele_freq = pd.read_csv("data/jsnp_allele_freq.csv")
    jsnp_allele_freq = jsnp_allele_freq[['allele-2 frequency']]



    return jsnp_allele_freq[:length].to_numpy()


if __name__ == '__main__':
    sys.setrecursionlimit(2500)
    argv = sys.argv[1:]
    length = 84716

    if len(argv) == 1:
        length = int(argv[0])

    l = 4
    m = int(length / l)
    path = "data/" + argv[0] + "_100000_1000_simulated/"
    # path = "data/84716_10_5_simulated/"
    raw_path = path + "raw.txt"
    target_path = "data/" + argv[0] + "_100000_1000_simulated_arranged_optimal"

    os.mkdir(target_path)

    probs = get_ps(length)
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





