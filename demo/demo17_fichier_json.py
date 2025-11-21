import json
import os

# --- Définition du chemin du fichier JSON ---
path = "./data.json"

# --- Lecture d'un fichier JSON ---
def lire_json(filepath):
    """
    Lit un fichier JSON et retourne son contenu sous forme de dictionnaire.
    """
    if os.path.exists(filepath):  # Vérifie si le fichier existe
        try:
            with open(filepath, 'r', encoding="utf8") as fichier:
                data = json.load(fichier)  # Chargement du JSON en dictionnaire Python
                print("Données du fichier JSON :", data)
                return data
        except json.JSONDecodeError as e:
            print(f"Erreur lors du décodage du JSON : {e}")
            return None
    else:
        print("Le fichier JSON n'existe pas.")
        return None

# --- Écriture dans un fichier JSON (création si inexistant) ---
def ecrire_json(filepath, data):
    """
    Écrit des données dans un fichier JSON. Crée le fichier s'il n'existe pas.
    """
    try:
        with open(filepath, 'w', encoding="utf8") as fichier:
            json.dump(data, fichier, indent=4, ensure_ascii=False)  # Écriture formatée
        print("Données enregistrées avec succès dans le fichier JSON.")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier JSON : {e}")

# --- Vérification et création initiale du fichier JSON ---
def verifier_ou_creer_json(filepath):
    """
    Vérifie si un fichier JSON existe. S'il n'existe pas, il est créé avec des données par défaut.
    """
    if not os.path.exists(filepath):
        print("Le fichier JSON n'existe pas, création avec des valeurs par défaut.")
        ecrire_json(filepath, {"prénom": "Toto", "nom": "Tata"})
    else:
        print("Le fichier JSON existe déjà.")

# --- Conversion JSON <-> String ---
def convertir_dict_en_str(data):
    """
    Convertit un dictionnaire Python en une chaîne JSON formatée.
    """
    try:
        json_str = json.dumps(data, indent=4, ensure_ascii=False)  # Conversion en JSON string
        print("Dictionnaire converti en chaîne JSON :")
        print(json_str)
        return json_str
    except Exception as e:
        print(f"Erreur lors de la conversion en chaîne JSON : {e}")
        return None


def convertir_str_en_dict(json_str):
    """
    Convertit une chaîne JSON en dictionnaire Python.
    """
    try:
        data_dict = json.loads(json_str)  # Conversion en dictionnaire
        print("Chaîne JSON convertie en dictionnaire :")
        print(data_dict)
        return data_dict
    except json.JSONDecodeError as e:
        print(f"Erreur lors du chargement du JSON : {e}")
        return None

# --- Exécution des fonctions (décommenter pour tester) ---
verifier_ou_creer_json(path)
data = lire_json(path)
if data:
    json_str = convertir_dict_en_str(data)
    convertir_str_en_dict(json_str)