#! python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = pd.read_csv('data_1d.csv', header=None).values

x = A[:, 0]
y = A[:, 1]

# histogram i.e. graph displaying frequency distribution of x data points
# defaults to 10 buckets
plt.hist(x)
plt.show()

R = np.random.random(10000)

# changing the number of buckets
plt.hist(R, bins=20)
plt.show()

# to check the distribution of errors. Normal distribution assumption
y_actual = 2*x + 1
residuals = y - y_actual
plt.hist(residuals)
plt.show()
