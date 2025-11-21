# ---------------------------------------------------------------------
# Les Dictionnaires (dict)
# ---------------------------------------------------------------------

# Un dictionnaire stocke des paires clé-valeur.
# Chaque clé doit être unique, et les valeurs peuvent être de tout type.

# ---------------------------------------------------------------------
# Déclaration et manipulation de base
# ---------------------------------------------------------------------

etudiant = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès à une valeur via sa clé
print("Nom :", etudiant["nom"])



# Ajout et modification de valeurs
etudiant["note"] = 18       # Ajout d'une nouvelle clé
etudiant["age"] = 26        # Modification d'une clé existante
print("Dictionnaire mis à jour :", etudiant)

# Suppression d’une clé
del etudiant["ville"]
print("Dictionnaire après suppression :", etudiant)

# Vérifier si une clé existe
if "nom" in etudiant:
    print("La clé 'nom' est présente")

# Longueur du dictionnaire
print("Nombre d'éléments :", len(etudiant))

# ---------------------------------------------------------------------
# Parcourir un dictionnaire
# ---------------------------------------------------------------------

for cle, valeur in etudiant.items():
    print(f"{cle} : {valeur}")

# Obtenir toutes les clés et toutes les valeurs
cles = etudiant.keys()
valeurs = etudiant.values()
print("Clés :", list(cles))
print("Valeurs :", list(valeurs))


# ---------------------------------------------------------------------
# Exemple de dictionnaire contenant des types variés
# ---------------------------------------------------------------------

donnees = {
    "id": 123,
    "nom": "Bob",
    "actif": True,
    "notes": [15, 18, 20],
    "adresse": {"ville": "Lyon", "code_postal": 69000},
    "moyenne": lambda notes: sum(notes) / len(notes)
}

print("Dictionnaire mixte :", donnees)
print("Longueur du dictionnaire mixte :", len(donnees))
print("Moyenne des notes :", donnees["moyenne"](donnees["notes"]))

# ---------------------------------------------------------------------
# Effacer tous les éléments d'un dictionnaire
# ---------------------------------------------------------------------

etudiant.clear()
print("Dictionnaire après effacement :", etudiant)
