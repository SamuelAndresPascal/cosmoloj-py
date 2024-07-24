import numpy as np

a = np.arange(start=1, stop=5)

print(a)

b = a[:2].copy()

b += 1

print(b)
print(a)
