import random

def recherche_dichotomique(tab, x):
    debut = 0
    fin = len(tab) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == x:
            return milieu
        elif tab[milieu] > x:
            fin = milieu - 1
        else:
            debut = milieu + 1

    return -1

taille_tab = 20
tab = sorted(random.sample(range(1, 101), taille_tab))

print("Voici le tableau :", tab)

x = random.randint(1, 100)
print("Nous allons rechercher le nombre", x, "dans le tableau.")

resultat = recherche_dichotomique(tab, x)

if resultat != -1:
    print("Le nombre", x, "se trouve à l'index", resultat, "dans le tableau.")
else:
    print("Le nombre", x, "n'est pas présent dans le tableau.")
