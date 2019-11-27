#! python3

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]])
v = np.array([1/3, 1/3, 1/3])
print(A)
print(v)

y = []

for i in range(25):
    v1 = v.dot(A)
    #y.append(abs((v1*v1)-(v*v)))
    y.append(np.linalg.norm(v1-v))
    v = v1

print(v1)
plt.plot(y)
plt.show()
