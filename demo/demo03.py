# Les opérateurs sont utilisés pour effectuer des opérations sur des variables et des valeurs.

# 1. Opérateurs arithmétiques
# Ces opérateurs permettent de réaliser des calculs mathématiques.
a = 10
b = 3

print(f"Addition : {a} + {b} = {a + b}")  # Addition
print(f"Soustraction : {a} - {b} = {a - b}")  # Soustraction
print(f"Multiplication : {a} * {b} = {a * b}")  # Multiplication
print(f"Division : {a} / {b} = {a / b}")  # Division
print(f"Division entière : {a} // {b} = {a // b}")  # Division entière
print(f"Modulo : {a} % {b} = {a % b}")  # Reste de la division
print(f"Exponentiation : {a} ** {b} = {a ** b}")  # Puissance

# 2. Opérateurs de comparaison
# Ces opérateurs comparent deux valeurs et retournent un booléen (True ou False).
print(f"{a} est-il égal à {b} ? {a == b}")  # Égalité
print(f"{a} est-il différent de {b} ? {a != b}")  # Différent
print(f"{a} est-il supérieur à {b} ? {a > b}")  # Supérieur
print(f"{a} est-il inférieur à {b} ? {a < b}")  # Inférieur
print(f"{a} est-il supérieur ou égal à {b} ? {a >= b}")  # Supérieur ou égal
print(f"{a} est-il inférieur ou égal à {b} ? {a <= b}")  # Inférieur ou égal

# 3. Opérateurs logiques
# Ces opérateurs permettent de combiner des expressions logiques.
x = True
y = False

print(f"Opérateur AND : {x} and {y} = {x and y}")  # ET logique
print(f"Opérateur OR : {x} or {y} = {x or y}")  # OU logique
print(f"Opérateur NOT : not {x} = {not x}")  # NON logique


# 4. Opérateurs d'affectation
# Ces opérateurs permettent d'affecter des valeurs aux variables.
c = 5
print(f"Valeur initiale de c : {c}")
c += 2  # Équivaut à c = c + 2
print(f"Après c += 2 : {c}")
c -= 1  # Équivaut à c = c - 1
print(f"Après c -= 1 : {c}")
c *= 3  # Équivaut à c = c * 3
print(f"Après c *= 3 : {c}")
c /= 2  # Équivaut à c = c / 2
print(f"Après c /= 2 : {c}")
c **= 2  # Équivaut à c = c ** 2
print(f"Après c **= 2 : {c}")


# 5. Opérateurs d'appartenance
# Ces opérateurs permettent de vérifier si une valeur appartient à une séquence.
# Ici, nous utilisons une liste, qui est un type de structure de données permettant de stocker plusieurs valeurs.
# Nous verrons les listes plus en détail dans une prochaine section.
ma_liste = [1, 2, 3, 4, 5]
print(f"3 est-il dans la liste ? {3 in ma_liste}")
print(f"10 est-il dans la liste ? {10 in ma_liste}")
print(f"6 n'est-il pas dans la liste ? {6 not in ma_liste}")

nom = "toto"
print("zzz" in nom)

print(f"Répétition de chaîne : {'Python ' * 3}")  # * répète la chaîne

