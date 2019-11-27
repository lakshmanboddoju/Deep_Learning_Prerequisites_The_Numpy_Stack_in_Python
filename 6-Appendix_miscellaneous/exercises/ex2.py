#! python3

import numpy as np
import matplotlib.pyplot as plt

# Visualizing the Central Limit Theorem

N = 1000
y = []
for i in range(N):
    y.append(np.random.random(N).sum())

plt.hist(y, bins=20)
plt.show()
