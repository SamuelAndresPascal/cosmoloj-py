import numpy as np

x = np.arange(10)
print(x[2])

print(x[-2])

x.shape = (2, 5)

print(x[1, 3])

print(x[1, -1])  # now x is 2-dimensional

print(x[0])  # get the first line

print(x[0, :])  # idem

print(x[:, 0]) # get the first column

print(x)

print(x[0, 2])

print(x[0][2])
