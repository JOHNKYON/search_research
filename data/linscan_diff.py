import heapq
import sys
import time


def linear_scan(path, query, k):
    """
    This function do linear scan kNN search on the raw data in the
    given path, a given query and a given k.


    :param path:
    :param query:
    :param k:
    :return:
    """
    file_path = path + "/raw.txt"
    candidates = []
    with open(file_path, 'r') as file:
        length = int(file.readline())
        data_size = int(file.readline())
        query_size = int(file.readline())
        print("Querying...")
        print("Query size:\t" + str(query_size))
        for i in range(data_size):
            string = file.readline().rstrip()
            relatedness = get_relatedness(query, string)
            if len(candidates) < k:
                heapq.heappush(candidates, [relatedness, i])

            elif len(candidates) >= k and relatedness > candidates[0][0]:
                heapq.heappop(candidates)
                heapq.heappush(candidates, [relatedness, i])

    idx = []
    for candidate in candidates:
        idx.append(candidate[1]+1)

    print("Done.")
    return idx


def get_relatedness(a, b):
    """
    >>> get_relatedness("0012", "0111")
    3

    >>> get_relatedness("0022", "0022")
    8

    :param a:
    :param b:
    :return:
    """
    assert len(a) == len(b)

    score = 0
    for i in range(len(a)):
        if a[i] == '0' or b[i] == '9':
            continue
        elif a[i] == '1' and b[i] == '1':
            score += 1
        elif a[i] == '1' or b[i] == '1':
            score += 2
        else:
            score += 4
    return score


def compare_results(res1, res2):
    """
    >>> compare_results([[1,3,2],[0,9,3]], [[3,1,2], [3,0,9]])
    True

    >>> compare_results([[1,3,2],[0,9,1]], [[3,1,2], [3,0,9]])
    False

    :param res1:
    :param res2:
    :return:
    """

    assert len(res1) == len(res2)

    for i in range(len(res1)):
        temp1 = sorted(res1[i])
        temp2 = sorted(res2[i])
        for j in range(len(temp1)):
            if temp1[j] != temp2[j]:
                return False

    return True


def load_query(path):
    file_path = path + "/raw.txt"
    query = []
    with open(file_path, 'r') as file:
        length = int(file.readline())
        data_size = int(file.readline())
        query_size = int(file.readline())
        for _ in range(data_size):
            file.readline()
        for _ in range(query_size):
            query.append(file.readline().rstrip())
    return query


if __name__ == '__main__':
    args = sys.argv[1:]
    path = args[0]
    k = int(args[1])

    # Linear Scan
    queries = load_query(path)

    # Search and store results
    with open(path + "/linscan.csv", 'w') as output:
        for query in queries:
            res = linear_scan(path, query, k)
            for idx in res:
                output.write(str(idx) + ',')
            output.write('\n')



