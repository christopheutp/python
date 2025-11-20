# L'opérateur ternaire permet d'écrire une condition simple en une seule ligne.
# Il remplace un bloc if-else court pour rendre le code plus concis et lisible.

# Syntaxe :
# variable = valeur_si_vrai if condition else valeur_si_faux

# 1. Exemple de base
age = 20
statut = "Majeur" if age >= 18 else "Mineur"
print(f"Statut : {statut}")  # Affiche 'Majeur'

# 2. Utilisation avec des nombres
nombre = 10
parite = "Pair" if nombre % 2 == 0 else "Impair"
print(f"Le nombre {nombre} est {parite}.")

# 3. Utilisation avec des booléens
connecte = True
message = "Utilisateur connecté" if connecte else "Utilisateur déconnecté"
print(message)

# 4. Exemple avec une valeur retournée
score = 85
mention = "Excellent" if score > 80 else "Passable"
print(f"Mention : {mention}")

# Récapitulatif
# - L'opérateur ternaire est utile pour simplifier des conditions courtes.
# - Il améliore la lisibilité du code lorsqu'une seule action est nécessaire.
# - Il ne doit pas être abusé pour des conditions complexes, au risque de nuire à la compréhension.