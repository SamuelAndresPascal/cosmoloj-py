import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(x[1:7:2])  # from 1 included to 7 excluded with a step of 2

print(x[-2:10])

print(x[10:-2])  # empty

print(x[10:-2:-1])  # but using a negative step, inverse the elements

print(x[-3:3:-1])

print(x[5:])

print(x[:5])

x = np.array([[[1],[2],[3]], [[4],[5],[6]]])

print(x.shape)

print(x[1:2])
