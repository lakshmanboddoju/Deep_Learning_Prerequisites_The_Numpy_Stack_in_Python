import numpy as np

Z = np.zeros(10)
print(Z)

Z = np.zeros((10, 10))
print(Z)

O = np.ones((10, 10))
print(O)

# Uniform distribution between 0 and 1
R = np.random.random((10, 10))
print(R)

# Gaussian distribution with mean 0 and variance 1
G = np.random.randn(10, 10)
print(G)
print(G.mean())
print(G.var())
