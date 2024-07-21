import numpy as np

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(c.shape)
print(c.dtype)

d = np.array([[1, 2], [3, 4]])
print(d)
print(d.shape)
print(d.dtype)

e = np.array([[1 + 1.j, 2 + 1.j], [3 + 1.j, 4 + 1.j]], dtype=complex)
print(e)
print(e.shape)
print(e.dtype)
