#! python3

import matplotlib.pyplot as plt
import numpy as np

# generates data with start point, end point and the num. of points in between (in that order)
x = np.linspace(0, 10, 10)

# Sine wave
y = np.sin(x)

print(plt.plot(x, y))
plt.xlabel("Time")
plt.ylabel("Some function of Time")
plt.title("My cool chart")
plt.show()

x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)
plt.plot(x1, y1)
plt.show()
