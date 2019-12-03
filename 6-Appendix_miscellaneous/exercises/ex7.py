#! python3

import numpy as np
import matplotlib.pyplot as plt

def plotDonut():
    N = 2000
    inRad = 5
    outRad = 15

    # Formula for a cirle centered on the origin with radius r is x^2 + y^2 = r^2
    # So x = r * cosT
    # y = r * sinT
    # where T is distributed between 0 and 2pi

    # distance from origin is radius + random normal
    # angle theta is uniformly distributed between (0, 2pi)
    R1 = inRad + np.random.randn(N//2) 
    theta = 2*np.pi*np.random.random(N//2)
    X_inner = np.array([R1 * np.cos(theta), R1 * np.sin(theta)]).T

    R2 = outRad + np.random.randn(N//2)
    X_outer = np.array([R2 * np.cos(theta), R2 * np.sin(theta)]).T

    plt.scatter(X_inner[:, 0], X_inner[:, 1])
    plt.scatter(X_outer[:, 0], X_outer[:, 1]) 
    plt.show()

plotDonut()
