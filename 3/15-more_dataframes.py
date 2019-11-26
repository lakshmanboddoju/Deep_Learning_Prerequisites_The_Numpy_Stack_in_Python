#! python3

import pandas as pd
import numpy as np

X = pd.read_csv("data_2d.csv", header=None)
M = X.values # can use .as_matrix() or .to_numpy() as well


print(type(M))

# Returns a column with name 0. not row
print(X[0])
print(type(X[1]))

# To get the row in a df obj
print(X.iloc[0])
print(X.ix[0])

# All 1-D arrays are called as series whereas 2-D arrays are dataframes
print(type(X.ix[0]))

# Selecting multiple columns at the same time. 0th and 2nd column:
print(X[[0,2]])

# Selecting specific rows matching certain criteria.
print(X[ X[0] < 5])
print(X[0] < 5)

# Again its a 1-D series
print(type(X[0] < 5))
