def is_safe(tableau, lign, col, N):
    # Vérifie si une dame peut être placée sur la case (lign, col)
    # Vérifie la colonne
    for i in range(lign):
        if tableau[i][col] == 1:
            return False

    # Vérifie la diagonale gauche supérieure
    for i, j in zip(range(lign, -1, -1), range(col, -1, -1)):
        if tableau[i][j] == 1:
            return False

    # Vérifie la diagonale droite supérieure
    for i, j in zip(range(lign, -1, -1), range(col, N)):
        if tableau[i][j] == 1:
            return False

    return True

def solve_n_queens_util(tableau, lign, N):
    # Cas de base : toutes les dames sont placées
    if lign >= N:
        return True

    # Essayer de placer une dame sur chaque colonne de cette rangée
    for col in range(N):
        if is_safe(tableau, lign, col, N):
            tableau[lign][col] = 1

            # Récursivement placer les dames sur les rangées suivantes
            if solve_n_queens_util(tableau, lign + 1, N):
                return True

            # Si placer une dame dans la colonne courante ne conduit pas à une solution, backtrack
            tableau[lign][col] = 0

    # Si aucune colonne ne mène à une solution, retourne False
    return False

def solve_n_queens(N):
    tableau = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(tableau, 0, N):
        print("Aucune solution n'existe.")
        return False

    # Affichage de la solution
    for lign in tableau:
        print(" ".join(map(str, lign)))
    return True

# Exemple d'utilisation
N = 8  # Taille du plateau N x N
solve_n_queens(N)
