import numpy as np

a = np.array([2, 3, 4], dtype=np.uint32)
print(a)

b = np.array([5, 6, 7], dtype=np.uint32)
print(b)

c = a - b  # c type is unsigned !!!
print(c)

d = a - b.astype(np.int32)  # d type is signed
print(d)
