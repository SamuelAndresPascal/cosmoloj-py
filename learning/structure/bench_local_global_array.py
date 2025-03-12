import time

# on utilise dans une boucle une valeur constante
# on veut mesurer le coût d'instanciation de ce tableau dans la boucle par rapport à sa déclaration à l'extérieur
# comme une constante globale

##########################
# cas d'un tableau de str
##########################

A = ["tata", "toto"]

start = time.time_ns()
for i in range(1000000):
    a = ["toto", "tata"]
    b = a[1] + a[0]

print((time.time_ns() - start) / 10**9)

start = time.time_ns()
for i in range(1000000):
    b= A[1] + A[0]

print((time.time_ns() - start) / 10**9)


########################################################
# cas d'un tableau d'objets non mis en cache par Python
########################################################

class Example:

    def __init__(self, arg: str):
        self._a = arg

    def a(self) -> str:
        return self._a


E = Example("tata")

start = time.time_ns()
for i in range(1000000):
    e = Example("toto")
    e.a()

print((time.time_ns() - start) / 10**9)


start = time.time_ns()
for i in range(1000000):
    E.a()

print((time.time_ns() - start) / 10**9)

