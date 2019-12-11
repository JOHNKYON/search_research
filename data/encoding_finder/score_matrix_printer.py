import pandas as pd

def print_encoding(l):
    bits_array = build_bits_array(l)
    score_matrix = build_score_matrix(bits_array)

    print(pd.DataFrame(score_matrix))

    return None





def build_bits_array(l):
    array = []
    string = ""
    append_digit(string, array, l)
    return array

def append_digit(s, array, l):
    """
    Recursively append 0 or 1 to a string until the length of s is l.
    Then add the s into array.
    :param s:
    :param array:
    :param l:
    :return:
    """
    if len(s) == l:
        array.append(s)
        return

    append_digit(s + "0", array, l)
    append_digit(s + "1", array, l)

def build_score_matrix(bits_array):
    score_matrix = []
    l = len(bits_array)
    for i in range(l):
        score_matrix.append([])
        for j in range(l):
            score_matrix[i].append(hd_score(bits_array[i], bits_array[j]))

    return score_matrix


def hd_score(s1, s2):
    score = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            score += 1
    return score

if __name__ == '__main__':
    # matrix = [[2,1,0],
    #           [1,1,1],
    #           [0,1,2]]
    matrix = [[0,0,0],
              [0,1,2],
              [0,2,4]]
    print_encoding(4)