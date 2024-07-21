import numpy as np

a = np.ones(shape=3, dtype=np.int32)

b = np.linspace(start=0, stop=np.pi, num=3)

print(b.dtype.name)

c = a + b

print(c)
print(c.dtype.name)

d = np.exp(c * 1j)
print(d)
print(d.dtype.name)
