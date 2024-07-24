import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

b = a > 4
print(b)

# 1d array with selected elements
print(a[b])

# update an array using a boolean index array
a[b] = 0
print(a)
