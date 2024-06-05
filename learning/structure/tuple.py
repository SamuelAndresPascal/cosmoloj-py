# construction à partir d'un autre tuple
l1 = tuple((1, 2, 3))

print(l1)
print(l1[0])
print(type(l1))

# litéral
l2 = (1, 2, 3)

print(l2)
print(l2[0])
print(type(l2))

# construction à partir d'une liste
l3 = tuple([1, 2, 3])

print(l3)
print(l3[0])
print(type(l3))

# construction à partir d'un générateur
l4 = tuple(i for i in range(1, 4))

print(l4)
print(l4[0])
print(type(l4))

# construction à partir d'un itérateur
l5 = tuple(range(1, 4))

print(l5)
print(l5[0])
print(type(l5))
