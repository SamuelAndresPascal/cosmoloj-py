import numpy as np

rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((3, 4)))

print(a)
print(a.shape)

print(a.ravel())  # returns the array, flattened
print(a.ravel(order='C'))  # default order is C-style
print(a.ravel(order='F'))  # use fortran-style !!!
print(a.flat)  # not an array !!!

print(a.reshape(6, 2))

print(a.T)  # transpose

print(a.T.shape)

print(a.shape)


print(a.resize(6, 2))  # resize() returns None !!!
print(a)  # but resize() modifies the array itself !!!
print(a.shape)

print(a.reshape(3, -1))  # "-1", means the dimension si automatically calculated
