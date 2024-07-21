import numpy as np

A = np.array([[1, 1],
              [0, 1]])

B = np.array([[2, 0],
              [3, 4]])

print(A * B)     # elementwise product

print(A @ B)     # matrix product

print(A.dot(B))  # another matrix product
