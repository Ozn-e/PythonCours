import random

# Liste de mots pour le jeu
words = [
    "python", "ordinateur", "programmation", "algorithme", "reseau",
    "securite", "informatique", "developpement", "logiciel", "internet",
    "serveur", "base_de_donnees", "virtualisation", "cloud", "cryptographie",
    "intelligence", "artificielle", "machine_learning", "cyberspace", "systeme"
]

# Choisir un mot au hasard
word = random.choice(words)
word_letters = set(word)
guessed_letters = set()

# Dessins du pendu pour chaque étape
hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\   |
      / \   |
            |
    =========
    """,
]

# Variables pour le jeu
max_attempts = len(hangman_stages) - 1
attempts = 0

# Fonction pour afficher le mot avec les lettres devinées
def display_word():
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Boucle principale du jeu
while attempts < max_attempts:
    print(hangman_stages[attempts])
    print("Mot: ", display_word())
    print(f"Lettres devinées: {', '.join(guessed_letters)}")

    guess = input("Devinez une lettre: ").lower()

    if guess in guessed_letters:
        print("Vous avez déjà deviné cette lettre.")
    elif guess in word:
        guessed_letters.add(guess)
    else:
        guessed_letters.add(guess)
        attempts += 1

    if set(word) <= guessed_letters:
        print("Félicitations, vous avez trouvé le mot:", word)
        break
else:
    print(hangman_stages[attempts])
    print("Vous avez perdu. Le mot était:", word)
