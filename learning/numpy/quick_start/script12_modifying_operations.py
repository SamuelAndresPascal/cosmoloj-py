import numpy as np

rg = np.random.default_rng(1)  # create instance of default random number generator

a = np.ones((2, 3), dtype=int)

b = rg.random((2, 3))

a *= 3
print(a)

b += a
print(b)

a += b  # b is not automatically converted to integer type
print(a)
