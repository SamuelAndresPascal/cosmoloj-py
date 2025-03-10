import time

a = []
start = time.time_ns()
for i in range(1000000):
    a.append(i)

print((time.time_ns() - start) / 10**9)

a = []
start = time.time_ns()
for i in range(1000000):
    a += [i]

print((time.time_ns() - start) / 10**9)
