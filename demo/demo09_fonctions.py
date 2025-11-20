
# En Python, une fonction est définie avec le mot-clé `def`, suivi :
#  - d'un NOM de fonction
#  - de PARENTHESES `()` contenant éventuellement des PARAMÈTRES
#  - d'un DEUX-POINTS `:` pour indiquer le début du bloc d'instructions
#  - d'un INDENTATION (espace ou tabulation) pour écrire les instructions de la fonction
#  - éventuellement d'un `return` pour renvoyer une valeur

# Syntaxe générale :
# def nom_de_la_fonction(paramètre1, paramètre2, ...):
#     instructions
#     return valeur (facultatif)

def saluer():
    # Affiche un message de salutation
    print("Bonjour tout le monde !")

# Appel de la fonction
saluer()  # Affiche "Bonjour tout le monde !"

def saluer_personne(nom):
    # Affiche un message de bienvenue personnalisé avec un nom
    print(f"Bonjour, {nom} !")

# Appel de la fonction avec un argument
saluer_personne("Alice")  # Affiche "Bonjour, Alice !"


def addition(a, b):
    # Retourne la somme de deux nombres
    return a + b

# Stocker et afficher le résultat
resultat = addition(5, 3)
print(f"Résultat de l'addition : {resultat}")  # Affiche 8

def bienvenue(nom="Invité"):
    # Affiche un message de bienvenue avec un nom par défaut
    print(f"Bienvenue, {nom} !")

# Appels de la fonction avec et sans argument
bienvenue("Bob")      # Affiche "Bienvenue, Bob !"
bienvenue()           # Affiche "Bienvenue, Invité !"

def greet(name: str = "toto") -> str:
    """
    Cette fonction prend un nom en entrée et affiche un message de bienvenue.
    :param name: str, le nom de la personne à saluer
    :return: str, le message de bienvenue
    """
    return f"Bonjour, {name} !"

print(greet())
print(greet("tata"))
print(greet.__doc__)
print(help(greet))


# En Python, il existe un type spécial de fonction appelé **fonction lambda**.
# Il s'agit d'une fonction **anonyme** (sans nom) qui tient sur une seule ligne.
# Elle est principalement utilisée pour des opérations simples et rapides.

# Syntaxe d'une fonction lambda :
# lambda paramètres: expression

# Exemple classique d'une fonction normale pour additionner deux nombres :
def addition_normale(x, y):
    return x + y

# Équivalent avec une fonction lambda :
addition_lambda = lambda x, y: x + y

# Appels des fonctions
print(addition_normale(2, 3))  # Affiche 5
print(addition_lambda(2, 3))   # Affiche 5


# Fonction lambda utilisée directement dans `print`
print((lambda a, b: a * b)(3, 4))  # Affiche 12


# Autre exemple : extraction du premier caractère d'une chaîne
premier_caractere = lambda texte: texte[-1]

print(premier_caractere("Python"))  # Affiche "P"