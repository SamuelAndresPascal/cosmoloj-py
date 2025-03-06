import time

a = [[0 for _ in range(10000)] for _ in range(10000)]

start = time.time_ns()
for i in a:
    for j in i:
        j = j + 1

print((time.time_ns() - start) / 10**9)

print(type(a))


b = [[]]
print(type(b))

def toto_local() -> str:
    a = ["toto", "tata"]
    b= a[1] + a[0]
    return b

A = ["tata", "toto"]
def toto_global() -> str:
    b= A[1] + A[0]
    return b

start = time.time_ns()
for i in range(1000000):
    toto_local()

print((time.time_ns() - start) / 10**9)



start = time.time_ns()
for i in range(1000000):
    toto_global()

print((time.time_ns() - start) / 10**9)

start = time.time_ns()
for i in range(1000000):
    toto_local()

print((time.time_ns() - start) / 10**9)



start = time.time_ns()
for i in range(1000000):
    toto_global()

print((time.time_ns() - start) / 10**9)


class Example:

    def __init__(self, arg: str):
        self._a = arg

    def a(self) -> str:
        return self._a


def tata_local() -> Example:
    e = Example("toto")
    return e

E = Example("tata")
def tata_global() -> Example:
    return E

start = time.time_ns()
for i in range(1000000):
    tata_local()

print((time.time_ns() - start) / 10**9)


start = time.time_ns()
for i in range(1000000):
    tata_global()

print((time.time_ns() - start) / 10**9)

start = time.time_ns()
for i in range(1000000):
    tata_local()

print((time.time_ns() - start) / 10**9)


start = time.time_ns()
for i in range(1000000):
    tata_global()

print((time.time_ns() - start) / 10**9)
