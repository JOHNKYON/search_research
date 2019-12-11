import math

def find_encoding(matrix, length):
    print(length)
    bits_array = build_bits_array(length)
    score_matrix = build_score_matrix(bits_array)
    l = len(bits_array)
    idxes = []
    diff = 10000
    for col0 in range(l):
        for col1 in range(l):
            for col2 in range(l):
                for row0 in range(l):
                    for row1 in range(l):
                        for row2 in range(l):
                            temp_idxes = [[col0, col1, col2],
                                        [row0, row1, row2]]
                            temp_diff = cal_diff(matrix, build_matrix(score_matrix, temp_idxes))
                            if temp_diff < diff:
                                diff = temp_diff
                                idxes = temp_idxes

    show_results(bits_array, idxes)
    print(build_matrix(score_matrix, idxes))
    print(cal_diff(matrix, build_matrix(score_matrix, idxes)))
    return None


def show_results(bits, idxes):
    for array in idxes:
        print(bits[array[0]] + '\t' + bits[array[1]] + '\t' + bits[array[2]])


def cal_diff(base_matrix, matrix):
    zero = matrix[2][0]
    four = matrix[2][2]
    if zero >= four:
        return 1000

    diff = 0

    # Change matrix to pivot matrix
    t = (four - zero) / base_matrix[2][2]

    for i in range(3):
        for j in range(3):
            matrix[i][j] = (matrix[i][j] - zero ) / t
            if matrix[i][j] < 0:
                return 1000
            diff += abs(base_matrix[i][j] - matrix[i][j])
    # print(diff)
    return diff

def build_matrix(score_matrix, indices):
    res = []
    for row in indices[1]:
        r = []
        for col in indices[0]:
            r.append(score_matrix[row][col])
        res.append(r)
    return res




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
    print(find_encoding(matrix, 4))