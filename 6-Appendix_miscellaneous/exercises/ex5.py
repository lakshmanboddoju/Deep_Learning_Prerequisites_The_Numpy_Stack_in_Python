#! python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def isSymmetric(matrix):
    return np.all(matrix == matrix.T)

def isSymmetric2(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        return False

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] != matrix[j, i]:
                return False
            
    return True

def main():

    A = np.zeros((3, 3))
    print("A: " + str(isSymmetric(A)))

    B = np.eye(5)
    print("B: " + str(isSymmetric2(B)))

    C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("C: " + str(isSymmetric2(C)))

    D = np.array([[1, 2], [2, 4]])
    print("D: " + str(isSymmetric(D)))

main()
