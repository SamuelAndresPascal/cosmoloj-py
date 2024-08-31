# construction à partir d'un tuple
from collections.abc import Iterator

l1 = list((1, 2, 3))

print(l1)
print(l1[0])
print(type(l1))

# litéral
l2 = [1, 2, 3]

print(l2)
print(l2[0])
print(type(l2))

# construction à partir d'une autre liste
l3 = list([1, 2, 3])

print(l3)
print(l3[0])
print(type(l3))

# construction par liste d'intention
l4 = [i for i in range(1, 4)]

print(l4)
print(l4[0])
print(type(l4))

if None:
    print("none is true")
else:
    print("none is false")

if []:
    print("empty list is true")
else:
    print("empty list is false")
