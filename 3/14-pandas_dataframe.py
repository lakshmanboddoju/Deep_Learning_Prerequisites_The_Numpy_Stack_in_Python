#! python3

import pandas as pd

X = pd.read_csv("data_2d.csv", header=None)
print(type(X))
print(X.info())
print(X.head())
print(X.head(10))
