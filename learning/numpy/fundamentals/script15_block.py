import numpy as np

a = np.ones((2, 2))

b = np.eye(N=2, M=2)

c = np.zeros((2, 2))

d = np.diag((-3, -4))

print(np.block([[a, b], [c, d]]))
