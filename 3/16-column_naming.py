#! python3

import pandas as pd

df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)

print(df.columns)
df.columns = ["month", "passengers"]

print(df.columns)

# Can call column values using column names. If column name is string can do .columnName as long as no space.
print(df["passengers"])
print(df.month)

# Adding coloumns and initializes with common value to each row
df["ones"] = 1
print(df.head())
