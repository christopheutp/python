import csv

# --- Lecture d'un fichier CSV et affichage du contenu ---
# Méthode classique avec ouverture et fermeture manuelle du fichier

def lire_csv(filepath):
    """
    Lit un fichier CSV et affiche son contenu ligne par ligne.
    """
    try:
        fichier = open(filepath, "rt", encoding="UTF-8")  # Ouverture en mode lecture (text mode)
        reader = csv.reader(fichier, delimiter=";")  # Création d'un lecteur CSV avec le délimiteur ;
        for row in reader:  # Parcours de chaque ligne du fichier
            print(row)  # Affichage du contenu de la ligne
        fichier.close()  # Fermeture du fichier
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

# --- Écriture dans un fichier CSV (écrase le fichier existant) ---

def ecrire_csv(filepath):
    """
    Écrit des lignes dans un fichier CSV. Ce mode écrase le contenu existant.
    """
    try:
        fichier = open(filepath, "wt", newline="", encoding="UTF-8")  # Ouverture en mode écriture
        writer = csv.writer(fichier, delimiter=";")  # Création d'un écrivain CSV
        writer.writerow(["Nom", "Âge", "Ville"])  # Écriture de l'en-tête (facultatif)
        writer.writerow(["Titi", 66, "Au pif"])  # Ajout de plusieurs lignes de données
        writer.writerow(["Toto", 88, "Lille"])
        writer.writerow(["Tata", 24, "Paris"])
        fichier.close()  # Fermeture du fichier
        print("Données écrites avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")

# --- Lecture avec "with open" (gestion automatique de la fermeture du fichier) ---

def lire_csv_with(filepath):
    """
    Lit un fichier CSV en utilisant le gestionnaire de contexte "with".
    """
    try:
        with open(filepath, mode='r', encoding="UTF-8") as fichier:
            reader = csv.reader(fichier, delimiter=";")
            for row in reader:
                print(row)
                for element in row:  # Affichage élément par élément
                    print(element)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

# --- Ajout de données dans un fichier CSV (mode append) ---

def ajouter_donnees_csv(filepath):
    """
    Ajoute de nouvelles lignes sans écraser les données existantes.
    """
    try:
        with open(filepath, mode='a', encoding="UTF-8", newline="") as fichier:
            writer = csv.writer(fichier, delimiter=";")
            writer.writerow(["Loick", 16, "Playstation"])
            writer.writerow(["Emma", 20, "Nintendo"])
        print("Données ajoutées avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout des données : {e}")

# --- Exécution des fonctions (décommenter pour tester) ---
filepath = "./test.csv"  # Remplace par le chemin correct si nécessaire
ecrire_csv(filepath)
lire_csv(filepath)
ajouter_donnees_csv(filepath)
lire_csv_with(filepath)
