#! python3

import pandas as pd

# Demenstrating joins with two tables

t1 = pd.read_csv("table1.csv")
t2 = pd.read_csv("table2.csv")

print(t1)
print(t2)

# .merge is equivalent to sql joins
m = pd.merge(t1, t2, on='user_id')
print(m)
print(t1.merge(t2, on='user_id'))
