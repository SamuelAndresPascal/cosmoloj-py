import numpy as np

a = np.array([[0, 1,  2,  3],
              [4, 5,  6,  7],
              [8, 9, 10, 11]])

c = a.view()

print(c is a)

print(type(a))
print(type(c))  # c is a ndarray !!!
print(c.base is a)  # c is a view of the data owned by a

print(a.flags.owndata)
print(c.flags.owndata)

c = c.reshape((2, 6))
print(c.shape)
print(a.shape)  # a's shape doesn't change

print(a)
print(c)
c[0, 4] = 1234
print(c)
print(a)  # a's data changes !!!


# slicing an array returns a view of it !!!!
s = a[:, 1:3]
s[:] = 10  # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10

print(a)
