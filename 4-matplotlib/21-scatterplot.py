#! python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = pd.read_csv('data_1d.csv', header=None).values

x = A[:, 0]
y = A[:, 1]

plt.scatter(x, y)
plt.show()

# Return evenly spaced numbers over a specified interval.
x_line = np.linspace(0, 100, 100)
y_line = 2*x_line + 1

plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.show()
