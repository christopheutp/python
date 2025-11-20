# Commentaires en Python :
# Un commentaire est un texte ignoré par l'interpréteur Python.
# Il commence par le symbole '#' et permet d'ajouter des explications dans le code.

# Exemple de commentaire :
# Cette ligne ne sera pas exécutée par Python


# La fonction print()
# Cette fonction permet d'afficher du texte ou des valeurs à l'écran.
print("Bonjour, bienvenue dans cette introduction à Python !")

# Vous pouvez afficher du texte entre guillemets simples ou doubles :
print('Ceci est un message affiché avec print')

# Afficher plusieurs éléments en les séparant par des virgules :
print("Le nombre", 42, "est un entier.")

# Afficher plusieurs éléments en utilisant la concaténation de chaînes :
print("Le " + "nombre " + "42" + " est" + " un" + " entier.")

# Afficher plusieurs éléments avec une f-string (recommandé) :
nombre = 42
print(f"Le nombre {nombre} est un entier.")

# Afficher plusieurs éléments avec la méthode format()
print("Le nombre {} est un entier.".format(42))

# La fonction input()
# Cette fonction permet de récupérer une saisie utilisateur au clavier.
nom = input("Quel est votre nom ? ")  # L'utilisateur doit entrer son nom
print("Bonjour", nom, "! Ravi de vous rencontrer.")

# Principe d'indentation en Python
# Python utilise l'indentation (espaces ou tabulations) pour définir les blocs de code.
# Chaque bloc de code imbriqué doit être correctement indenté avec 4 espaces.

# Exemple d'indentation correcte avec une structure conditionnelle :
age = int(input("Quel est votre âge ? "))  # Convertir l'entrée utilisateur en entier

if age >= 18:
    print("Vous etes majeur")

    # Règles de bonnes pratiques en Python
# 1. Utiliser des noms de variables explicites (éviter x, y, z sauf pour les maths).
# 2. Respecter la convention de nommage :
#    - snake_case pour les variables et fonctions : exemple_variable
#    - PascalCase pour les classes : ExempleClasse
#    - CONSTANTES en majuscules : EXEMPLE_CONSTANTE
# 3. Ajouter des commentaires clairs mais éviter d'en abuser.
# 4. Respecter la PEP 8 (guide de style de Python).

