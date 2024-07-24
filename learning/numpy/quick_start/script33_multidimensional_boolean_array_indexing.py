import numpy as np

a = np.arange(12).reshape(3, 4)

b1 = np.array([False, True, True])         # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection

print(a[b1, :])                                   # selecting rows

print(a[b1])                                      # same thing

print(a[:, b2])                                   # selecting columns

print(a[b1, b2])                                  # a weird thing to do
