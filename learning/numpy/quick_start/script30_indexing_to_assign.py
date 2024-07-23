import numpy as np

# indexing for multiple assignation

a = np.arange(5)

print(a)

# multiple assignation of a single value
a[[1, 3, 4]] = 0

print(a)

a = np.arange(5)

print(a)

# multiple assignation of several values
a[[1, 3, 4]] = [4, 5, 6]

print(a)

a = np.arange(5)

print(a)

# repeted indices are allowed but erase previous ones
a[[0, 0, 2]] = [1, 2, 3]

print(a)

a = np.arange(5)

print(a)

# increment several indices
a[[1, 3, 4]] += 1

print(a)

a = np.arange(5)

print(a)

# incrementation with repeted indices: the 0th element is incremented only once
a[[0, 0, 2]] += 1

print(a)
