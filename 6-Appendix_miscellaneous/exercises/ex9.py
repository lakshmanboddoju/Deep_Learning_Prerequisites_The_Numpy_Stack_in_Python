#! python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from ex8 import get_spiral

# get the data
X, Y = get_spiral()

# combine the data into one array
# data to be concatenated must have same # of dimensions
# e.g. N x D and N x 1
# not  N x D and N
data = np.concatenate((X, np.expand_dims(Y, 1)), axis=1)

df = pd.DataFrame(data)
df.columns = ['x1', 'x2', 'y']
df.to_csv('mydata.csv', index=False)
