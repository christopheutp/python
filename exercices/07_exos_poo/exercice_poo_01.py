# Exercice : Classe Gateau

# Objectif :
# - Créer une classe `Gateau` permettant de représenter une recette de gâteau.
#
# Étapes :
# 1. Définir la classe `Gateau`.
# 2. Ajouter les attributs suivants et les initialiser dans le constructeur :
#    - `nom_gateau` (str) : Nom du gâteau.
#    - `temps_cuisson` (int) : Temps de cuisson en minutes.
#    - `ingredients` (list de str) : Liste des ingrédients.
#    - `etapes_recette` (list de str) : Liste des étapes de préparation.
#    - `nom_createur` (str) : Nom du créateur de la recette.
# 3. Ajouter une méthode qui affiche les ingrédients de la recette.
# 4. Instancier un objet `Gateau` et afficher ses ingrédients ainsi que les étapes de préparation.


class Gateau:
    """
    Classe représentant une recette de gâteau.
    """
    def __init__(self, nom_gateau: str, temps_cuisson: int, ingredients: list, etapes_recette: list, nom_createur: str):
        """
        Initialise un objet Gateau avec ses attributs.
        """
        self.nom_gateau = nom_gateau
        self.temps_cuisson = temps_cuisson
        self.ingredients = ingredients
        self.etapes_recette = etapes_recette
        self.nom_createur = nom_createur
    
    def afficher_ingredients(self):
        """
        Affiche la liste des ingrédients du gâteau.
        """
        print(f"Ingrédients pour {self.nom_gateau} :")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
    
    def afficher_recette(self):
        """
        Affiche les étapes de préparation de la recette.
        """
        print(f"\nPréparation du {self.nom_gateau} par {self.nom_createur} (Temps de cuisson : {self.temps_cuisson} min) :")
        compteur = 1
        for etape in self.etapes_recette:
            print(f"Étape {compteur}: {etape}")
            compteur += 1


def main():
    """
    Fonction principale pour créer et afficher une recette de gâteau.
    """
    # Instanciation d'un objet Gateau
    mon_gateau = Gateau(
        nom_gateau="Fondant au chocolat",
        temps_cuisson=30,
        ingredients=["200g de chocolat noir", "100g de beurre", "100g de sucre", "3 œufs", "50g de farine"],
        etapes_recette=["Faire fondre le chocolat et le beurre.", "Mélanger avec le sucre et les œufs.", "Ajouter la farine et bien mélanger.", "Verser dans un moule et enfourner à 180°C pendant 30 minutes."],
        nom_createur="Chef Pâtissier"
    )

    # Affichage des ingrédients et de la recette
    mon_gateau.afficher_ingredients()
    mon_gateau.afficher_recette()

if __name__ == "__main__":
    main()