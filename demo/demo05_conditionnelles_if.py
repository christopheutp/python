# Une structure conditionnelle permet d'exécuter différentes parties du code
# en fonction d'une condition donnée.
# Python utilise les mots-clés 'if', 'elif' et 'else' pour gérer les conditions.

# 1. Condition simple avec if
# La condition 'if' permet d'exécuter un bloc de code si une expression est vraie.
# Exemple : Vérifier si une personne est majeure
age = 20
if age >= 18:  # Si la condition est vraie
    print("Vous êtes majeur.")  # Ce bloc est exécuté
    print("une instruction suivante")

# Si la condition est fausse, rien ne se passe.

# 2. Condition avec if et else
# L'instruction 'else' permet de définir un bloc de code exécuté si la condition est fausse.
age = 16
if age >= 18:
    print("Vous êtes majeur.")  # Si la condition est vraie
else:
    print("Vous êtes mineur.")  # Sinon, ce bloc est exécuté

# 3. Condition avec if, elif et else
# 'elif' signifie "else if" et permet de tester plusieurs conditions successives.
# Python évalue les conditions dans l'ordre, et exécute le premier bloc dont la condition est vraie.
age = 15
if age < 12:
    print("Vous êtes un enfant.")  # Vérifie si l'âge est inférieur à 12
elif age < 18:
    print("Vous êtes un adolescent.")  # Si la première condition est fausse, vérifie cette condition
else:
    print("Vous êtes un adulte.")  # Si aucune condition précédente n'est vraie, ce bloc est exécuté

# Remarque : Dès qu'une condition est vraie, les conditions suivantes ne sont pas évaluées.
# Exemple : Si age = 15, 'print("Vous êtes un adolescent.")' est exécuté et la suite est ignorée.

# 4. Opérateurs de comparaison et logiques dans les conditions
# - == (égal à)
# - != (différent de)
# - < (inférieur à)
# - > (supérieur à)
# - <= (inférieur ou égal à)
# - >= (supérieur ou égal à)
# - and (ET logique)
# - or (OU logique)
# - not (NON logique)

nom = "Alice"
age = 22

if age >= 18 and nom == "Alice":
    print("Alice est majeure.")

if age < 18 or nom == "Bob":
    print("Cette personne est soit mineure, soit elle s'appelle Bob.")

if not age < 18:
    print("Cette personne est majeure.")

# 5. Conditions imbriquées
# On peut imbriquer des conditions pour tester plusieurs cas successifs.

temperature = 30
if temperature > 25:
    print("Il fait chaud.")
    if temperature > 35:
        print("Il fait très chaud ! Hydratez-vous.")
    else:
        print("Profitez du soleil, mais restez prudent.")
else:
    print("Le temps est agréable.")

# 6. Expression conditionnelle (Opérateur ternaire)
# En Python, on peut utiliser une expression conditionnelle en une seule ligne.

note = 15
resultat = "Réussi" if note >= 10 else "Échec"
print(f"Résultat de l'examen : {resultat}")

# 7. L'instruction pass
# L'instruction 'pass' permet d'écrire une structure conditionnelle sans action immédiate.

nom_utilisateur = ""
if nom_utilisateur:
    print(f"Bienvenue, {nom_utilisateur}")
else:
    pass  # Cette ligne évite une erreur si le bloc else est vide


# 8. Vérification de valeurs avec in
# On peut vérifier si une valeur est dans une liste, un tuple ou une chaîne.

voyelles = "aeiou"
lettre = "e"
if lettre in voyelles:
    print(f"{lettre} est une voyelle.")

jours_ouverts = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
jour_actuel = "samedi"
if jour_actuel not in jours_ouverts:
    print(f"{jour_actuel.capitalize()} est un jour de repos.")

# 9. Vérification des types avec isinstance
# Pour s'assurer qu'une variable est d'un type spécifique, on peut utiliser isinstance().

valeur = 42
if isinstance(valeur, int):
    print("La variable est un entier.")