from sys import argv
import os
import copy

POSSIBLE_DIRECTIONS = "udrlwxyz"


def check_input_args(args):
    if len(args) == 4:

        if os.path.exists(args[0]) == False and os.path.exists(
                args[1]) == False:

            return "Error: Invalid/non-existent word list"
        elif os.path.exists(args[0]) == False:

            return "Error: Invalid/non-existent word list"
        elif os.path.exists(args[1]) == False:
            return "Error: Invalid/Non-existent matrix"
        for letter in args[3]:

            if letter not in POSSIBLE_DIRECTIONS:

                return "Error: Invalid direction letter"
            else:
                continue
        return None
    else:
        return "Invalid numbers of parameters (!=4)"


def read_wordlist_file(filename):
    with open(filename, 'r') as wordfile:
        word_list = [line.strip() for line in wordfile]
    return word_list


def read_matrix_file(filename):
    matrix = []
    list_letter = []

    with open(filename, 'r') as matrixfile:
        for line in matrixfile:
            for letter in line:
                if letter != ',' and letter != '\n':
                    list_letter.append(letter)
                else:
                    continue
            matrix.append(list_letter)
            list_letter = []
    return matrix


def word_in_list(word, word_list, results):
    if word in word_list:
        if word not in results:
            results[word] = 1
            return True
        else:
            results[word] += 1
            return True
    else:
        return False


def check_rlud(word_list, matrix):
    test_word = ''
    results = {}
    for row in matrix:
        for i in range(len(row)):
            for j in range(i, len(row)):
                test_word += row[j]
                if word_in_list(test_word, word_list, results):
                    continue
            test_word = ""

    return results


def matrix_l(matrix):
    for row in matrix:
        row[:] = row[::-1]


def matrix_d(matrix):
    final = [[matrix[j][i] for j in
              range(len(matrix))] for i in range(len(matrix[0]))]

    return final


def check_wxyz(wordlist, matrix):
    temp_result1 = {}
    temp_result2 = {}
    my_list = []
    for i in range(len(matrix)):
        for j1 in range(min(i + 1, len(matrix[0]))):
            for j2 in range(j1, min(i + 1, len(matrix[0]))):
                s = []
                for j in range(j1, j2 + 1):
                    s.append(matrix[i - j][j])
                my_list.append(''.join(s))

    for testword in my_list:
        if word_in_list(testword, wordlist, temp_result1):
            continue

    my_list2 = []
    for j in range(1, len(matrix[0])):
        for i1 in range(0, len(matrix[0]) - j):
            for i2 in range(i1 + 1, len(matrix[0]) - j + 1):
                k = []
                for i in range(i1, i2):
                    k.append(matrix[len(matrix) - i - 1][j + i])
                my_list2.append(''.join(k))
    for word in my_list2:
        if word_in_list(word, wordlist, temp_result2):
            continue

    results = sum_result(temp_result1, temp_result2)
    return results


def sum_result(dict1, dict2):
    result = {}
    for key, val in dict1.items():
        for k, l in dict2.items():
            if key == k:
                c = {key: val + l}
                result.update(c)
    for key, val in dict1.items():
        if key not in result:
            result.update({key: val})
    for m, n in dict2.items():
        if m not in result:
            result.update({m: n})

    return result


def find_words_in_matrix(word_list, matrix, directions):
    if matrix == []:
        results = {}
        return dict_to_list(results)
    """
    DICT TO LIST OF TUPLES!

    :param word_list:
    :param matrix:
    :param directions:
    :return:
    """
    f_directions = list(set(directions))

    results = {}

    for direc in f_directions:
        if direc == "r":
            temp_results = check_rlud(word_list, matrix)
            results = sum_result(results, temp_results)
        elif direc == "l":
            temp_mat = copy.deepcopy(matrix)
            matrix_l(temp_mat)
            temp_results = (check_rlud(word_list, temp_mat))
            results = sum_result(results, temp_results)
        elif direc == "d":
            temp_mat = copy.deepcopy(matrix)
            transposed = matrix_d(temp_mat)
            temp_results = check_rlud(word_list, transposed)
            results = sum_result(results, temp_results)
        elif direc == "u":
            temp_mat = copy.deepcopy(matrix)
            transposed = matrix_d(temp_mat)
            matrix_l(transposed)
            temp_results = check_rlud(word_list, transposed)
            results = sum_result(results, temp_results)
        elif direc == "w":
            temp_mat = copy.deepcopy(matrix)
            temp_results = check_wxyz(word_list, temp_mat)
            results = sum_result(results, temp_results)
        elif direc == "x":
            temp_mat = copy.deepcopy(matrix)
            matrix_l(temp_mat)
            temp_results = check_wxyz(word_list, temp_mat)
            results = sum_result(results, temp_results)
        elif direc == "z":
            temp_mat = copy.deepcopy(matrix)
            transposed = matrix_d(temp_mat)
            temp_results = check_wxyz(word_list, transposed)
            results = sum_result(results, temp_results)
        elif direc == "y":
            temp_mat = copy.deepcopy(matrix)
            temp_mat2 = matrix_d(temp_mat)
            matrix_l(temp_mat2)
            transposed = matrix_d(temp_mat2)
            temp_results = check_wxyz(word_list, transposed)

            results = sum_result(results, temp_results)

    return dict_to_list(results)


def dict_to_list(result_dict):
    list1 = list(result_dict.items())
    return list1


def write_output_file(results, output_filename):

    if results == []:
        open(output_filename, 'w').close()

    with open(output_filename, "w") as file:
        for t in results:
            file.write(','.join(str(s) for s in t) + '\n')


def main():
    check = check_input_args(argv[1:5])
    if check is None:
        word_list = argv[1]
        matrix = argv[2]
        output_file = argv[3]
        directions = argv[4]

        wordlist = read_wordlist_file(word_list)
        matrix_used = read_matrix_file(matrix)
        results = find_words_in_matrix(wordlist, matrix_used, directions)
        write_output_file(results, output_file)

    else:
        return check


if __name__ == '__main__':
    main()
