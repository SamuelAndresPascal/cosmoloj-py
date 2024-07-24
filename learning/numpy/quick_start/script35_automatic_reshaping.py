import numpy as np

a = np.arange(30)

b = a.reshape((2, -1, 3))  # -1 means "whatever is needed"

print(b.shape)

print(b)
