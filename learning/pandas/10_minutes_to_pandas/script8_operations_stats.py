import numpy as np
import pandas as pd

dates = pd.date_range(start="20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df.loc[:, "D"] = np.array([5] * len(df))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

# setting by column
df["F"] = s1

print(df)

print(df.mean())

print(df.mean(axis=1))

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

print(s)

# substract series to all columns
print(df.sub(s, axis="index"))

s2 = pd.Series([1, 3, 5, np.nan, 6], index=list("ABCDF")).shift(2)

print(s2)

# substract series to all lines
print(df.sub(s2, axis="columns"))
