import numpy as np

# Vandermonde matrices

print(np.vander(np.linspace(start=0, stop=2, num=5), N=2))

print(np.vander(x=[1, 2, 3, 4], N=2))

print(np.vander(x=[1, 2, 3, 4], N=4))
