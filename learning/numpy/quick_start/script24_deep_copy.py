import numpy as np

a = np.array([[0, 1,  2,  3],
              [4, 5,  6,  7],
              [8, 9, 10, 11]])

d = a.copy()  # a new array object with new data is created

print(d is a)

print(d.base is a)  # d doesn't share anything with a


d[0, 0] = 9999

print(d)
print(a)

# Sometimes copy should be called after slicing if the original array is not required anymore. For example, suppose a
# is a huge intermediate result and the final result b only contains a small fraction of a, a deep copy should be made
# when constructing b with slicing:

huge = np.arange(int(1e8))
b = huge[:100]
del huge  # the memory of "a" can be released

print(b)

print(huge)  # "huge" may no longer exist

