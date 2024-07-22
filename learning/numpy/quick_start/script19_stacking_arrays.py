import numpy as np

rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((2, 2)))

print(a)
b = np.floor(10 * rg.random((2, 2)))

print(b)

print(np.vstack((a, b)))

print(np.hstack((a, b)))
