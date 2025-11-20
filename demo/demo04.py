# Une méthode est une fonction spécifique liée à un objet.
# Un objet est une instance d'un type de données (comme str, int, list, etc.).
# En Python, tout est un objet, ce qui signifie que nous pouvons utiliser des méthodes sur eux.

# Pour vérifier le type d'un objet, nous utilisons la fonction type()
texte = "   Bonjour, Python est génial!   "
print(f"Le type de l'objet texte est : {type(texte)}")  # Affiche <class 'str'>

# 1. Suppression des espaces inutiles
print(f"Avant strip(): '{texte}'")
print(f"Après strip(): '{texte.strip()}'")  # Supprime les espaces en début et fin

# 2. Conversion en majuscules et minuscules
print(f"En majuscules : {texte.upper()}")  # Convertit en majuscules
print(f"En minuscules : {texte.lower()}")  # Convertit en minuscules



# 3. Capitalisation 
print(f"Première lettre en majuscule : {texte.strip().capitalize()}")  # Met la première lettre en majuscule

# 4. Remplacement de texte
print(f"Remplacement de 'Python' par 'Java' : {texte.replace('Python', 'Java')}")

# 5. Vérification de contenu
print(f"Le texte commence-t-il par 'Bonjour' ? {texte.strip().startswith('Bonjour')}")
print(f"Le texte se termine-t-il par '!' ? {texte.strip().endswith('!')}")

# 6. Recherche dans une chaîne
print(f"Position de 'Python' : {texte.find('Python')}")  # Retourne l'index du premier caractère trouvé
print(f"Nombre d'occurrences de 'o' : {texte.count('o')}")


print(f"La chaîne contient-elle uniquement des lettres ? {texte.isalpha()}")  # False car il y a des espaces et des signes
print(f"La chaîne contient-elle uniquement des chiffres ? {'12345'.isdigit()}")  # True car uniquement des chiffres