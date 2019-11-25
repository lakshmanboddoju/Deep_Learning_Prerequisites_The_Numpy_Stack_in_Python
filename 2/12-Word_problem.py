#! python3

import numpy as np

# The admission fee at a small fair is $1.50 for children and $4.00 for adults. On a certain dat,
# 2000 people enter the fair and $5050 is collected. How many children and how many adults attended?

# X1 - num of children
# X2 - num of adults

# X1 + X2 = 2200
# 1.5 * X1 + 4 * X2 = 5050

A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])

x = np.linalg.solve(A, b)
print("Solution using numpy is: " + str(x))
print("i.e. numChild = " + str(x[0]) + " and numAdult = " + str(x[1]))
