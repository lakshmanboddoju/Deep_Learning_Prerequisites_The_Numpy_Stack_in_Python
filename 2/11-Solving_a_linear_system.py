#! python3

import numpy as np

# problem:  Ax = b where A - matrix, x - column vector and b - vector of numbers.
# solution: AInv * A * x = x = AInv * b multiply by AInv on both sides to solve for x.
# assumptions: in a system of D equations and D unknowns, A is a DxD Matrix, assuming its invertable.


A = np.array([[1, 2], [3, 4]])
print("A: " + str(A))

b = np.array([1, 2])
print("b: " + str(b))

x = np.linalg.inv(A).dot(b)
print("Solution for x in Ax = b is: " + str(x))

# Can also solve using numpy. Way more efficient.
x = np.linalg.solve(A, b)
print("Solution using numpy solve(): " + str(x))
