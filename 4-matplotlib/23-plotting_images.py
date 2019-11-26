#! python3

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv")

print(df.head())
print(df.shape)

M = df.values

img1 = M[0, 1:]
print(img1.shape)

# Reshape to a 28*28 matrix from 784 pixels
img1 = img1.reshape(28, 28)
print(img1.shape)

# plt.imshow(img1, cmap='gray')
plt.imshow(255-img1, cmap='gray')
plt.show()

# Check label
print(M[0, 0])
