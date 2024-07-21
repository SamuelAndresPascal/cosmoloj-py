import numpy as np

b = np.arange(12).reshape(3, 4)

print(b)
print(b.sum(axis=0))     # sum of each column
print(b.min(axis=1))     # min of each row

print(b.cumsum(axis=1))  # cumulative sum along each row

c = np.arange(8).reshape(2, 2, 2)

print(c)
print(c.sum(axis=0))
print(c.sum(axis=1))
print(c.min(axis=1))

print(c.cumsum(axis=1))  # cumulative sum along each row
