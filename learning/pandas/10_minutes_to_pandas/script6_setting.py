import numpy as np
import pandas as pd

dates = pd.date_range(start="20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

# setting by column
df["F"] = s1

print(df)

df.at[dates[0], "A"] = 0

print(df)

df.iat[0, 1] = 0

print(df)

df.loc[:, "D"] = np.array([5] * len(df))

print(df)

df2 = df.copy()

df2[df2 > 0] = -df2

print(df2)
