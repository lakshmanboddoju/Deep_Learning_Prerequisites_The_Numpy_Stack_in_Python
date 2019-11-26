#! python3

import pandas as pd
from datetime import datetime

# Creating a new column and adding values based on exisiting values in its row using apply.

df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
df.columns = ["month", "passengers"]
df["ones"] = 1

print(datetime.strptime("1949-05", "%Y-%m"))

# axis=1 is used to specify rows instead of columns
df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
print(df.info())
print(df.head())
