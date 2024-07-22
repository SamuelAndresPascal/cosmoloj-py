import numpy as np
from numpy import newaxis

rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((2, 2)))

print(a)
b = np.floor(10 * rg.random((2, 2)))

print(b)


print(np.column_stack((a, b)))

a = np.array([4., 2.])

b = np.array([3., 8.])

print(np.column_stack((a, b)))  # returns a 2D array

print(np.hstack((a, b)))        # the result is different

print(a[:, newaxis])  # view `a` as a 2D column vector

print(np.column_stack((a[:, newaxis], b[:, newaxis])))

print(np.hstack((a[:, newaxis], b[:, newaxis])))  # the result is the same
