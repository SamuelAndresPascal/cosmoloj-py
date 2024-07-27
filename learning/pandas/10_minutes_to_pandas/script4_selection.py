import numpy as np
import pandas as pd

dates = pd.date_range(start="20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df["A"])

# selection by __get_item__
print(df[0:3])

print(df["20130102":"20130104"])


# selecting by label
print(df.loc[dates[0]])

print(df.loc[:, ["A", "B"]])

print(df.loc["20130102":"20130104", ["A", "B"]])

print(df.loc[dates[0], "A"])

# get a specific row/column scalar
print(df.at[dates[0], "A"])


# selection by position
print(df.iloc[3])

print(df.iloc[3:5, 0:2])

print(df.iloc[[1, 2, 4], [0, 2]])

print(df.iloc[1:3, :])

print(df.iloc[:, 1:3])

print(df.iloc[1, 1])

print(df.iat[1, 1])

