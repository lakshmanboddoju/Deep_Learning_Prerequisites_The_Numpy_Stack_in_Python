import numpy as np
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

def slowDotProduct(a, b):
    result = 0
    for e, f in zip(a, b):
        result += e * f
    return result

t0 = datetime.now()
for t in range(T):
    slowDotProduct(a, b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
    a.dot(b)
dt2 = datetime.now() - t0

print("dt1 / dt2: ", dt1.total_seconds() / dt2.total_seconds())
