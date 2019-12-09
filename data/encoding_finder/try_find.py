import math

def find_encoding(matrix):
    length = int(math.log2(len(matrix)))
    ceil = 128
    while length < 128:
        print(length)
        bits_array = build_bits_array(length)
        score_matrix = build_score_matrix(bits_array)
        l = len(bits_array)
        for row0 in range(l-2):
            for col0 in range(l-2):
                for col1 in range(col0+1, l-1):
                    for col2 in range(col1+1, l):
                        score_row = score_matrix[row0]
                        if score_row[col0] == score_row[col1] and score_row[col0] == score_row[col2]:
                            pivot_zero = score_row[col0]
                            # Look for the second valid row
                            for row1 in range(l):
                                score_row = score_matrix[row1]
                                if score_row[col0] == pivot_zero:
                                    diff = score_row[col2] - score_row[col0]
                                    if diff != 0:
                                        # Look for the third valid row
                                        for row2 in range(l):
                                            score_row = score_matrix[row2]
                                            if score_row[col0] == pivot_zero and \
                                                    score_row[col2] == pivot_zero + 4 * diff:
                                                        return [[bits_array[col0], bits_array[col1], bits_array[col2]],
                                                        [bits_array[row0], bits_array[row1], bits_array[row2]]]
        length += 1

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
              [0,1,-1],
              [0,-1,4]]
    print(find_encoding(matrix))