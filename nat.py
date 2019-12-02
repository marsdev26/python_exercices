my_list = [''.join(matrix[len(matrix) - i - 1][j + i] for i in range(i1, i2))
           for j in range(1, len(matrix[0]))
           for i1 in range(0, len(matrix[0]) - j)
           for i2 in range(i1 + 1, len(matrix[0]) - j + 1)]
