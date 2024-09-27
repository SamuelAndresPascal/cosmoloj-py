# Exemple du risque posé par les arguments par défaut
# les paramètres a et b préexistent pour les fonctions foo et bar
# on ajoute pour chacune un paramètre 'added'
# la méthode foo n'a pas d'argument par défaut : l'oubli d'un argument provoque l'erreur de l'interpréteur
# la méthode bar a un argument par défaut pour b. Comme 'added' n'a pas de valeur par défaut, il doit être placé avant
# le paramètre b. Au moment de l'interprétation, la modification de la signature ne provoque pas d'erreur
# de l'interpréteur, mais provoque un bogue silencieux.

def foo(a: str, b: str, added: str):
    print('welcome into foo!')
    print("a = " + a)
    print("b = " + b)
    print("c = " + added)

def bar(a: str, added: str, b: str = 'default b'):
    print('welcome into bar!')
    print("a = " + a)
    print("b = " + b)
    print("c = " + added)

# bogue silencieux: l'ancienne valeur explicite du paramètre b est interprété comme la valeur du nouveau paramètre added
# la valeur par défaut est renseignée pour l'argument b
bar('a', 'b')

# erreur d'interprétation explicite
foo('a', 'b')
