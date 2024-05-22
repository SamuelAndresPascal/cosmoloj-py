import math


class Constant:

    @property
    def PI(self):
        return math.pi

    @property
    def E(self):
        return math.e


constant = Constant()  # il faut passer par une instance
print(constant.PI)  # on simule bien la syntaxe d'une constante mais en violant la convention des noms de fonctions
print(Constant.PI)  # on ne peut accéder à la valeur directement à partir de la classe sans passer par une instance

