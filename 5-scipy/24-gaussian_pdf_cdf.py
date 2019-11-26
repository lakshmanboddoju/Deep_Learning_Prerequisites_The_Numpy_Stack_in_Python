#! python3

from scipy.stats import norm
import numpy as np

# Gaussian Probability Density Function
# default mean = 0 and variance = 1
print(norm.pdf(0))

# Gaussian with mean == loc = 5 and standard deviation == scale = 10 == variance = 100
print(norm.pdf(0, loc=5, scale=10))

r = np.random.randn(10)
print(norm.pdf(r))

# Joint log probability
print(norm.logpdf(r))

# Cumulative Distribution function == integral of pdf from -infinity to x
print(norm.cdf(r))
print(norm.logcdf(r))
