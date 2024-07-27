import numpy as np
import pandas as pd

dates = pd.date_range(start="20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

# selecting rows
print(df[df["A"] > 0])

# selecting values !!!
print(df[df > 0])

# filtering

df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]

print(df2)

print(df2[df2["E"].isin(["two", "four"])])

print(df2["E"].isin(["two", "four"]))
print(type(df2["E"].isin(["two", "four"])))
