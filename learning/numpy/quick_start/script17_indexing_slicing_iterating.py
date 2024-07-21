import numpy as np

a = np.arange(10) ** 3

print(a)

print(a[2])

print(a[2:5])

# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
a[:6:2] = 1000

print(a)

print(a[::-1])

for i in a:
    print(i ** (1 / 3.))

# multidimentional arrays:


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, shape=(5, 4), dtype=int)

print(b)

print(b[2, 3])

print(b[0:5, 1])  # each row in the second column of b

print(b[:, 1])    # equivalent to the previous example

print(b[1:3, :])  # each column in the second and third row of b

print(b[-1])


# usage of dots

c = np.array([[[0, 1, 2],  # a 3D array (two stacked 2D arrays)
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])

print(c.shape)

print(c[1, ...])  # same as c[1, :, :] or c[1]

print(c[..., 2])  # same as c[:, :, 2]


# iterating over multidimentional array

for row in b:
    print(row)

for element in b.flat:
    print(element)
