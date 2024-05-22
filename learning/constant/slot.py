import math


class Constant:
    __slots__ = ()
    PI = math.pi
    E = math.e


print(Constant.PI)
c = Constant()
print(c.PI)
# c.PI = 2  # Attribute error : on ne peut pas modifier les valeurs de l'instance
Constant.PI = 2  # mais on peut modifier les valeurs globales !!
u = Constant()
print(u.PI)
