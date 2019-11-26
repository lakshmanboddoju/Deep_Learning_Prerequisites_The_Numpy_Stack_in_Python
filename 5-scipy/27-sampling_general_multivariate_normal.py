#! python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn

# covariance matrix variance = 1 in 1st dimension and var = 3 in 2nd. covariance between both is 0.8
cov =  np.array([[1, 0.8], [0.8, 3]])

mu = np.array([0, 2])

# Draw random samples from a multivariate normal distribution
r = mvn.rvs(mean=mu, cov=cov, size=1000)

plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()

# Using numpy to get the random samples
r1 = np.random.multivariate_normal(mean=mu, cov=cov, size=1000)

plt.scatter(r1[:, 0], r1[:, 1])
plt.axis('equal')
plt.show()
