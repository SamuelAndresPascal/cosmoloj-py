import numpy as np

a = np.array([[0, 1,  2,  3],
              [4, 5,  6,  7],
              [8, 9, 10, 11]])

b = a            # no new object is created

print(b is a)


def f(x):
    print(id(x))


print(id(a))
print(id(b))
f(a)
f(b)
