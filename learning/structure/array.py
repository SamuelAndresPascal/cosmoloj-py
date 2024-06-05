import time

a = [[0 for x in range(10000)] for y in range(10000)]

start = time.time_ns()
for i in a:
    for j in i:
        j = j + 1

print((time.time_ns() - start) / 10**9)

print(type(a))


b = [[]]
print(type(b))
