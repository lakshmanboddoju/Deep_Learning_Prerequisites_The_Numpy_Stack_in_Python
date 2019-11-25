#! python3

import numpy as np

A = np.array([[1, 2], [3, 4]])

AInv = np.linalg.inv(A)
print(AInv)
print(A.dot(AInv))
print(AInv.dot(A))

# Matrix Determinant
print(np.linalg.det(A))

# Diagonal
print(np.diag(A))

# Matrix with only diagonal elements
print(np.diag([1, 2, 3]))

# Outer product: used for covariance
# C(i, j) = A(i) * B(j)
# Differennt from the dot product / inner product i.e. C = sum_over_i(A(i) * B(i))
a = np.array([1, 2])
b = np.array([3, 4])

print(np.outer(a, b))
print(np.inner(a, b))

# Matrix Trace = sum of diagonals of the matrix
print(np.diag(A).sum())
print("Matrix Trace of A: " + str(np.trace(A)))

# Covariance 
X = np.random.randn(100, 3)
covarianceX = np.cov(X)
print("Covariance of X: " + str(covarianceX))
print("Shape of covariance of X: " + str(covarianceX.shape))
print("Incorrect shape, needs to be 3x3.")

covarianceX = np.cov(X.T)
print("Correct covariance of X: " + str(covarianceX))
print("Correct shape: " + str(covarianceX.shape))

# EigenValues and EigenVectors
# Symmetrc Matrix == True when Matrix A == A.T i.e matrix is equal to its transpose
# Hermitian Matrix == True when A == A.H i.e. matrix is equal to its conjugate transpose
print(np.linalg.eigh(covarianceX))
eigenValues, eigenVectors = np.linalg.eig(covarianceX)
print(eigenValues)
print(eigenVectors)

