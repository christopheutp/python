# =====================================================================
# Lecture et écriture dans un fichier en Python
# =====================================================================

# 1. Introduction
# En Python, on peut lire et écrire dans des fichiers texte grâce à la fonction intégrée open().
# Un fichier doit être "ouvert" avant d'être utilisé, puis "fermé" à la fin pour libérer les ressources.

# Modes d'ouverture les plus courants :
#  - "r" : lecture seule (read)
#  - "w" : écriture (écrase le fichier s'il existe)
#  - "a" : ajout à la fin du fichier (append)
#  - "r+" : lecture et écriture


# ---------------------------------------------------------------------
# 2. Écriture dans un fichier
# ---------------------------------------------------------------------

# Création d'un fichier et écriture ligne par ligne
fichier = open("exemple.txt", "w", encoding="utf-8")

fichier.write("Bonjour à tous !\n")
fichier.write("Ceci est une démonstration d'écriture dans un fichier.\n")
fichier.write("Python rend cela très simple.\n")

# Fermeture du fichier
fichier.close()
print("Fichier 'exemple.txt' créé et rempli avec succès.\n")


# ---------------------------------------------------------------------
# 3. Lecture complète du fichier avec read()
# ---------------------------------------------------------------------

fichier = open("exemple.txt", "r", encoding="utf-8")
contenu = fichier.read()
print("Contenu complet du fichier :")
print(contenu)
fichier.close()


# ---------------------------------------------------------------------
# 4. Lecture ligne par ligne avec une boucle
# ---------------------------------------------------------------------

fichier = open("exemple.txt", "r", encoding="utf-8")
print("Lecture ligne par ligne :")
for ligne in fichier:
    print(ligne.strip())  # strip() supprime le saut de ligne
fichier.close()


# ---------------------------------------------------------------------
# 5. Lecture avec readline() et readlines()
# ---------------------------------------------------------------------

fichier = open("exemple.txt", "r", encoding="utf-8")

# readline() lit une seule ligne à la fois
print("\nLecture avec readline() :")
premiere_ligne = fichier.readline()
print("Première ligne :", premiere_ligne.strip())

# readlines() lit toutes les lignes et les stocke dans une liste
fichier.seek(0)  # Revenir au début du fichier
lignes = fichier.readlines()
print("\nLecture avec readlines() (liste de lignes) :")
print(lignes)
fichier.close()


# ---------------------------------------------------------------------
# 6. Écriture multiple avec writelines()
# ---------------------------------------------------------------------

# writelines() écrit plusieurs lignes à la fois (sans ajout automatique de '\n')
nouvelles_lignes = [
    "Voici une première ligne ajoutée avec writelines().\n",
    "Et une deuxième ligne.\n",
    "Fin de l'ajout multiple.\n"
]

fichier = open("exemple.txt", "a", encoding="utf-8")
fichier.writelines(nouvelles_lignes)
fichier.close()
print("\nPlusieurs lignes ajoutées avec writelines().")


# ---------------------------------------------------------------------
# 7. Bonne pratique : utiliser 'with open(...)'
# ---------------------------------------------------------------------

# Le mot-clé 'with' ferme automatiquement le fichier même en cas d’erreur.

with open("exemple.txt", "a", encoding="utf-8") as f:
    f.write("Ligne ajoutée via 'with open()'.\n")

print("\nNouvelle ligne ajoutée avec 'with open()'.")

# Vérification du contenu final
with open("exemple.txt", "r", encoding="utf-8") as f:
    print("\nContenu final du fichier :")
    print(f.read())


# ---------------------------------------------------------------------
# 8. Résumé
# ---------------------------------------------------------------------

# - read() lit tout le fichier d’un coup (chaîne unique).
# - readline() lit une seule ligne à la fois.
# - readlines() lit toutes les lignes et renvoie une liste.
# - write() écrit une seule chaîne.
# - writelines() écrit plusieurs lignes d’un coup.
# - with open(...) ferme automatiquement le fichier.