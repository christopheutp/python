# Les structures itératives permettent d'exécuter un bloc de code plusieurs fois.
# Python propose deux principales boucles : 'for' et 'while'.

# 1. La boucle for
# La boucle 'for' permet d'itérer sur une séquence de nombres avec range().

# Exemple avec range()
for i in range(5):  # De 0 à 4 (5 exclus)
    print(f"Itération {i}")

# Boucle for avec un pas spécifique
for i in range(1, 10, 2):  # De 1 à 9 avec un pas de 2
    print(f"Nombre impair : {i}")

# 2. La boucle while
# La boucle 'while' exécute le code tant qu'une condition est vraie.

compteur = 0
while compteur < 5:
    print(f"Compteur : {compteur}")
    compteur += 1  # Incrémentation

# Attention aux boucles infinies ! Assurez-vous que la condition devient fausse à un moment donné.

# 3. Instructions break et continue
# 'break' permet d'interrompre une boucle prématurément.
# 'continue' permet de sauter une itération sans sortir de la boucle.

for i in range(10):
    if i == 5:
        break  # Arrête la boucle quand i vaut 5
    print(f"i = {i}")

for i in range(10):
    if i % 2 == 0:
        continue  # Passe à l'itération suivante si i est pair
    print(f"Nombre impair : {i}")

# 4. Utilisation de else avec les boucles
# 'else' dans une boucle s'exécute uniquement si la boucle se termine normalement (sans break).

for i in range(3):
    print(f"Tentative {i}")
else:
    print("La boucle s'est terminée normalement.")

# Si break est utilisé, le bloc else ne s'exécute pas.
for i in range(3):
    print(f"Tentative {i}")
    if i == 1:
        break
else:
    print("Ce message ne s'affichera pas.")

# 5. Boucles imbriquées
# On peut imbriquer des boucles pour exécuter des actions répétées à plusieurs niveaux.

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

        # 6. Itération sur des structures de données
# Python permet d'utiliser les boucles pour parcourir des structures comme les listes ou les dictionnaires.
# Nous verrons ces structures plus tard en détail.

# Exemple avec une liste
elements = ["Pomme", "Banane", "Cerise"]
for fruit in elements:
    print(f"Fruit : {fruit}")

# Exemple avec un dictionnaire
dictionnaire = {"nom": "Alice", "âge": 25, "ville": "Paris"}
for cle, valeur in dictionnaire.items():
    print(f"{cle} : {valeur}")

# Nous verrons plus en détail les listes et les dictionnaires dans une prochaine section.

# Récapitulatif
# - 'for' permet de parcourir une séquence de nombres avec range()
# - 'while' s'exécute tant qu'une condition est vraie
# - 'break' arrête une boucle, 'continue' saute une itération
# - 'else' après une boucle s'exécute uniquement si la boucle se termine sans break
# - Il est possible d'imbriquer des boucles
# - Les boucles permettent aussi de parcourir des structures de données, ce que nous verrons plus tard.