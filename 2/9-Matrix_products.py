import numpy as np
import traceback

# Matrix multiplication definition: C(i, j) = Sum_1_to_k(A(1, k) * B(k, j))
# (i,j)th entry of C is the dot product of row A(i, :) and column B(:, j)
# in numpy C = A.dot(B)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[1, 2], [3, 4], [5, 6]])

try:
    print("A.B: " + str(A.dot(B)))
    print("B.A: " + str(B.dot(A)))
except ValueError:
    print(traceback.format_exc())
