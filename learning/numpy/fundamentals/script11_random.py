from numpy.random import default_rng

print(default_rng(42).random((2, 3)))

print(default_rng(42).random((2, 3, 2)))
