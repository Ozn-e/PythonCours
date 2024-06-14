from collections import Counter

# Fonction pour calculer la fréquence d'apparition de chaque lettre
def calculer_frequences(texte):
    compteurs = Counter(c for c in texte if c.isalpha())
    total = sum(compteurs.values())
    return {c: compteurs[c] / total for c in compteurs}

# Fonction pour afficher les fréquences sous forme de barres
def afficher_barres(frequences):
    max_width = 40
    max_frequency = max(frequences.values())
    for lettre, freq in sorted(frequences.items()):
        bar_width = int(freq / max_frequency * max_width)
        print(lettre, '■' * bar_width)

# Demande à l'utilisateur d'entrer un texte
texte = input("Entrez un texte : ").lower()

frequences_lettres = calculer_frequences(texte)

afficher_barres(frequences_lettres)