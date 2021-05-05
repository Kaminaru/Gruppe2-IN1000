def sjekkStigende(liste):
    for i in range(len(liste) - 1): # 0 til 3
        if liste[i] > liste[i+1]:
            return False
    return True

print(sjekkStigende([1,3,4,7,10]))




def lagSynonymordbok(listeAvLister):
    ordbok = {}
    for liste in listeAvLister:
        for synonym in liste:
            if synonym not in ordbok:
                ordbok[synonym] = []

            listeAvAndreSynonymer = []
            for ord in liste:
                if synonym != ord:
                    listeAvAndreSynonymer.append(ord)
            ordbok[synonym].append(listeAvAndreSynonymer)
            #print(ordbok)
    return ordbok

synonymer = [["a", "e", "i", "o", "u"],
            ["HOM", "c", "d"],
            ["y", "HOM"],
            ["k", "l", "m", "n", "p", "q"],
            ["x"]]
synonymordbok = lagSynonymordbok(synonymer)
assert synonymordbok["e"] == [["a", "i", "o", "u"]]
assert synonymordbok["a"] == [["e", "i", "o", "u"]]
assert synonymordbok["u"] == [["a", "e", "i", "o"]]
assert synonymordbok["c"] == [["HOM", "d"]]
assert synonymordbok["HOM"] == [["c", "d"], ["y"]]
assert synonymordbok["x"] == [[]]