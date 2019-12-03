#! python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# generate unlabeled data
N = 2000
X = np.random.random((N, 2))*2 - 1

# generate labels
Y = np.zeros(N)
Y[(X[:,0] < 0) & (X[:,1] > 0)] = 1
Y[(X[:,0] > 0) & (X[:,1] < 0)] = 1

# plot it
plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()
