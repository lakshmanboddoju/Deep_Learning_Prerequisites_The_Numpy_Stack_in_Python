#! python3

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

r = np.random.randn(10000)

plt.hist(r, bins=100)
plt.show()

# Mean is 5 and variance is 10 standard deviation
r1 = 10*np.random.randn(10000) + 5
plt.hist(r1, bins=100)
plt.show()
