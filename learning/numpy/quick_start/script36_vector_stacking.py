import numpy as np

x = np.arange(0, 10, 2)

y = np.arange(5)

m = np.vstack([x, y])

print(m)

xy = np.hstack([x, y])

print(xy)
