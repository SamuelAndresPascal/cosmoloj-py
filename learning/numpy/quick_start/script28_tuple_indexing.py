import numpy as np

a = np.arange(12).reshape(3, 4)

i = np.array([[0, 1],  # indices for the first dim of `a`
              [1, 2]])

j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])

print(a[i, j])  # i and j must have equal shape

l = (i, j)
print(a[l])

print(a[(i, j)])

s = [i, j]
print(a[tuple(s)])

print(a[s])  # does not support arrays as indices => only for assignation purpose !!!
