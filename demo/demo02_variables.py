# import this

# Une variable est un conteneur qui stocke une valeur.
# En Python, une variable est créée dès qu'on lui assigne une valeur.

# Déclaration et affectation de variables
nom = "Alice"  # Variable de type chaîne de caractères (str)
age = 25       # Variable de type entier (int)
taille = 1.75  # Variable de type flottant (float)
est_majeur = True  # Variable de type booléen (bool)

# Affichage des variables
print(f"Nom : {nom}")
print(f"Âge : {age}")
print(f"Taille : {taille}m")
print(f"Majeur : {est_majeur}")

# La fonction type()
# La fonction type() permet de connaître le type d'une variable.
# C'est utile pour vérifier si une variable contient bien le type attendu.
# Exemples :
print(type("Bonjour"))  # Affichera <class 'str'>
print(type(42))          # Affichera <class 'int'>
print(type(3.14))        # Affichera <class 'float'>
print(type(True))        # Affichera <class 'bool'>

# Vérification du type d'une variable avec type()
print(f"Type de nom : {type(nom)}")
print(f"Type de age : {type(age)}")
print(f"Type de taille : {type(taille)}")
print(f"Type de est_majeur : {type(est_majeur)}")

# Changement de valeur d'une variable
nom = "Bob"
print(f"Nouveau nom : {nom}")

# Assignation multiple (affectation simultanée)
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# Échange de valeurs entre deux variables
x, y = y, x
print(f"Après échange : x = {x}, y = {y}")

# Concaténation de chaînes de caractères
message = "Bonjour " + nom + " !"
print(message)

# Conversion de types (casting)
annee_naissance = "1998"  # Chaîne de caractères
annee_naissance = int(annee_naissance)  # Conversion en entier
print(f"Année de naissance : {annee_naissance}")

# Vérification du type après conversion
print(f"Type de annee_naissance après conversion : {type(annee_naissance)}")

# Conversion en booléen (bool casting)
# En Python, certaines valeurs sont évaluées à False par défaut :
# - False
# - 0 (zéro)
# - "" (chaîne vide)
# - [] (liste vide)
# - {} (dictionnaire vide)
# - None (absence de valeur)


valeur1 = 0
valeur2 = "Python"
valeur3 = []
valeur4 = None

print(f"Conversion de {valeur1} en booléen : {bool(valeur1)}")  # False
print(f"Conversion de '{valeur2}' en booléen : {bool(valeur2)}")  # True
print(f"Conversion de {valeur3} en booléen : {bool(valeur3)}")  # False
print(f"Conversion de {valeur4} en booléen : {bool(valeur4)}")  # False