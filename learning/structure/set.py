
def test_set1():

    # l'ordre de parcours des éléments d'un set :
    # 1. ne préserve pas l'ordre d'insertion donné par la list
    # 2. semble identique pour tous les parcours d'une exécution
    # 3. mais varie d'une exécution à l'autre
    l = ['conda', 'pip']
    first_count = {'conda': 0, 'pip': 0}
    for i in range(1000):
        s = set(l)
        for e in s:
            first_count[e] += 1
            break

    print(first_count)

def test_set2():

    # en passant par les clefs d'un dictionnaire, on préserve l'ordre des éléments
    # tout en garantissant leur unicité
    l = ['conda', 'pip']
    first_count = {'conda': 0, 'pip': 0}
    for i in range(1000):
        s = list(dict.fromkeys(l))
        for e in s:
            first_count[e] += 1
            break

    print(first_count)
