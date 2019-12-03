#! python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
data = df.values

np.random.shuffle(data)

X = data[:, 1:]
Y = data[:, 0]

def rotClockwise(img):
    return np.rot90(img, 3)

def rotClockwise2(img):
    H, W = img.shape
    img2 = np.zeros((W, H))

    for i in range(H):
        for j in range(W):
            img2[j, H - i - 1] = img[i, j]
            
    return img2

def mainFn():

    for i in range(X.shape[0]):

        img = X[i].reshape(28, 28)
        img = rotClockwise(img)

        plt.imshow(img, cmap="gray")
        plt.title("Label: %s" % Y[i])
        plt.show()

        ans = input("Continue? [y/n]: ")
        if ans and ans[0].lower() == "n":
            break

mainFn()
