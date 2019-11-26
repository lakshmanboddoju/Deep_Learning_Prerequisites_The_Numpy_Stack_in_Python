#! python3

import matplotlib.pyplot as plt
import numpy as np

r = np.random.randn(10000, 2)

# Verifying that the points are distributed in a circular scatter plot
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()


# Elliptical gaussian when variances are different
r[:, 1] = 5*r[:, 1] + 2
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()
