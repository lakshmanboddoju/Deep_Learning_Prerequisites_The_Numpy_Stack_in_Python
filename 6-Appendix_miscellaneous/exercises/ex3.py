#! python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading image dataset
df = pd.read_csv("train.csv")
data = df.values
images = data[:, 1:]
labels = data[:, 0]

for k in range(10):
    imageK = images[labels == k]

    # Mean/avg image
    meanK = imageK.mean(axis=0)

    imReshaped = meanK.reshape(28, 28)

    plt.imshow(imReshaped, cmap="gray")
    plt.title("Label: %s" % k)
    plt.show()
