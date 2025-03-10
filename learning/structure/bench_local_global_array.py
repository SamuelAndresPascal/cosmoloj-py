import time

# on utilise dans une boucle une valeur constante
# on veut mesurer le coût d'instanciation de ce tableau dans la boucle par rapport à sa déclaration à l'extérieur
# comme une constante globale

##########################
# cas d'un tableau de str
##########################

def toto_local() -> str:
    a = ["toto", "tata"]
    b = a[1] + a[0]
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


########################################################
# cas d'un tableau d'objets non mis en cache par Python
########################################################

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

