import random

nombre = 0
nb_random = random.randint(1, 100)

while nb_random != nombre:
    nombre = int(input("Entrez un nombre entre 1 et 100 : "))
    if nombre > nb_random:
        print('Trop grand')
    elif nombre < nb_random:
        print('Trop petit')

print("Bien joué ! Le nombre était", nb_random)