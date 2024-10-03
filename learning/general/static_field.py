import dataclasses
from dataclasses import dataclass


class Toto:
    TITI = 2

class Tutu:
    TITI = 3

    def __init__(self, titi: int):
        self.TITI = titi


class Tata:

    def __init__(self, titi: int):
        self.TITI = titi

class Tete:
    TITI = 5

@dataclass
class Tyty:
    TITI = 4
    TUTU: int = 3

print("===Tutu===")
print(Toto.TITI) # accès au champ statique

toto1 = Toto()
toto2 = Toto()
print(hasattr(toto1, "TITI"))
print(hasattr(toto2, "TITI"))

print(toto1.TITI) # accès au champ statique vu comme un champ d'instance
print(toto2.TITI)

Toto.TITI = 1 # modification du champ statique (modifie la valeur pour toutes les instances)
print(toto1.TITI) # accès au champ statique vu comme un champ d'instance
print(toto2.TITI)

toto1.TITI = 4 # création à la volée d'un champ d'instance
print(toto1.TITI) # accès au champ d'instance
print(toto2.TITI) # accès au champ statique vu comme un champ d'instance
print(Toto.TITI)

Toto.TITI = 3 # création dynamique d'un champ d'instance
print(toto1.TITI) # accès au champ d'instance
print(toto2.TITI) # accès au champ statique vu comme un champ d'instance
print(Toto.TITI)

print("===Tutu===")
print(Tutu.TITI) # accès au champ statique

tutu1 = Tutu(titi=1) # ici on accède au champ d'instance
tutu2 = Tutu(titi=2)

print(tutu1.TITI)
print(tutu2.TITI)
tutu1.TITI = 4 # ici on accède au champ d'instance
print(tutu1.TITI)
print(tutu2.TITI)
print(Tutu.TITI) # on n'a pas touché au champ statique


print("===Tete===")
print(Tete.TITI)
tete1 = Tete()
tete2 = Tete()
print(tete1.TITI)
print(tete2.TITI)
Tete.TITI = 2 # modification du champ statique : on modifie le champ de toutes les instances
print(tete1.TITI)
print(tete2.TITI)
tete1.TITI = 3 # création à la volée d'un champ d'instance
print(tete1.TITI)
print(tete2.TITI)
Tete.TITI = 4 # modification du champ statique
print(tete1.TITI) # on accède au champ d'instance
print(tete2.TITI) # on accède au champ statique comme un champ d'instance


print("===Tata===")
tata = Tata(titi=1)
print(tata.TITI)
# print(Tata.TITI) # => erreur : le champ statique n'existe pas !

print("===Tyty===")
print(Tyty.TITI)
print(Tyty.TUTU)

tyty1 = Tyty(TUTU=2)
print(tyty1.TITI)
print(tyty1.TUTU)
tyty2 = Tyty()
print(tyty2.TITI)
print(tyty2.TUTU)

Tyty.TITI = 8
Tyty.TUTU = 9
print(tyty1.TITI) # champ statique via le champ d'instance
print(tyty1.TUTU) # le champ d'instance existant n'a pas été impacté par la modification du champ statique
print(tyty2.TITI) # champ statique via le champ d'instance
print(tyty2.TUTU) # le champ d'instance existant n'a pas été impacté par la modification du champ statique
print(Tyty.TITI)
print(Tyty.TUTU) # accès au champ statique disctict du champ d'instance ! :)
print("=")
dataclasses.fields(tyty1)
print("=")
dataclasses.fields(tyty2)
print("=")
dataclasses.fields(Tyty)

# tyty3 = Tyty(TITI=3) # erreur : le champt d'instance n'existe pas !
#print(tyty3.TITI)
#print(tyty3.TUTU)


