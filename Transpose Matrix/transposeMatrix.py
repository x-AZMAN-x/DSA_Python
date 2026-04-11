# Using List Comprehensions

def matrixTranspose1(matrix):
    # Returning The Transpose Of Matrix Represented As Lists Of Lists
    if not matrix or matrix[0]:
        return []
    return [[matrix[j][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]

matrix = [[1, 2, 3],
     [4, 5, 6]]
print("Transpose: ", matrixTranspose1(matrix))

# Numpy Way

import numpy as np
matrix_np = np.array([[1, 2, 3],
                      [4, 5, 6]])
print("Transpose:\n", matrix_np.T)

#More Naive Way

def matrixTranspose2(matrix):
    if not matrix:
        return []
    
    row = len(matrix)
    col = len(matrix[0])

    res = []

    for j in range(col):
        new_row = []
        for i in range(row):
            new_row.append(matrix[i][j])
        res.append(new_row)

    return res

matrix = [[10, 20, 30],
            [40, 50, 60]]
res = matrixTranspose2(matrix)
print(res)