"""
La Programmation Orientée Objet (POO) est un paradigme de programmation qui repose sur la notion d'objets.
Un objet est une entité qui regroupe des données (appelées attributs) et des comportements (appelés méthodes).

Pourquoi utiliser la POO ?
- **Modularité** : Le code est organisé en classes et objets, facilitant la réutilisation et la maintenance.
- **Encapsulation** : Les données sensibles peuvent être protégées et accessibles uniquement via des méthodes dédiées.
- **Héritage** : Permet de créer de nouvelles classes à partir d'existantes, favorisant la réutilisation.
- **Polymorphisme** : Différents objets peuvent partager des interfaces communes et se comporter différemment.

Que peut-on représenter avec la POO ?
- Un utilisateur dans une application web (ex : un compte utilisateur avec nom, email, mot de passe)
- Un véhicule dans un jeu vidéo (ex : une voiture avec vitesse, essence, marque)
- Un produit dans un système de gestion d'inventaire (ex : un livre avec titre, auteur, prix)

Voyons maintenant comment implémenter cela en Python.
"""

# 1. Définition d'une classe

class Personne:
    """
    Classe représentant une personne avec un nom et un âge.
    """

    def __init__(self, nom, age):
        """Le constructeur (__init__) permet d'initialiser les attributs d'un objet."""
        self.nom = nom  # Attribut public
        self.age = age  # Attribut public

    def se_presenter(self):
        """Méthode qui retourne une présentation de la personne."""
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."


# Création d'un objet (instance de la classe Personne)
personne1 = Personne("Alice",30)
print(personne1.se_presenter())
print(type(personne1))
print(personne1.age)
personne1.age = 34
print(personne1.se_presenter())


# 2. Encapsulation : restreindre l'accès à certains attributs
class CompteBancaire:
    """
    Classe représentant un compte bancaire avec un solde protégé.
    """
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire  # Attribut public
        self.__solde = solde  # Attribut privé (préfixé par __)

    def deposer(self, montant):
        """Ajoute de l'argent au compte."""
        self.__solde += montant
        print(f"{montant}€ ont été déposés. Solde actuel : {self.__solde}€")

    def retirer(self, montant):
        """Retire de l'argent si le solde est suffisant."""
        if montant <= self.__solde:
            self.__solde -= montant
            print(f"{montant}€ ont été retirés. Solde restant : {self.__solde}€")
        else:
            print("Fonds insuffisants !")

    def get_solde(self):
        """Accès sécurisé au solde."""
        return self.__solde
    


# Test de l'encapsulation
compte = CompteBancaire("Bob", 1000)
print(compte.titulaire)
# print(compte.__solde)
compte.deposer(500)
compte.deposer(500)
compte.retirer(300)
print(f"Solde final : {compte.get_solde()}€")


# 3. Héritage : une classe enfant hérite des propriétés et méthodes d'une classe parent
class Etudiant(Personne):
    """
    Classe Etudiant qui hérite de Personne.
    """
    
    def __init__(self, nom, age, filiere):
        super().__init__(nom, age)  # Appelle le constructeur de Personne
        self.filiere = filiere  # Nouvel attribut

    # def se_presenter(self):
    #     return f"{super().se_presenter()} et j'etudie {self.filiere}"

    def se_presenter(self):
        """Surcharge de la méthode pour inclure la filière."""
        return f"Je suis {self.nom}, j'ai {self.age} ans et j'étudie {self.filiere}."

# Test de l'héritage
etudiant1 = Etudiant("Charlie", 22, "Informatique")
print(etudiant1.se_presenter())

# 4. Polymorphisme : différentes classes peuvent avoir la même méthode mais un comportement différent
class Chien:
    def parler(self):
        return "Wouf Wouf !"

class Chat:
    def parler(self):
        return "Miaou !"

# Fonction utilisant le polymorphisme
animaux = [Chien(), Chat()]
for animal in animaux:
    print(animal.parler())

# 5. Méthodes spéciales : __str__, __len__, __eq__, etc.
class Livre:
    """
    Classe représentant un livre.
    """
    
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

    def __str__(self):
        """Affichage convivial d'un livre"""
        return f"{self.titre} de {self.auteur}, {self.pages} pages."
    
    def __len__(self):
        """Retourne le nombre de pages."""
        return self.pages

livre1 = Livre("1984", "George Orwell", 328)
print(livre1) 
print(f"Nombre de pages : {len(livre1)}")


# 6. Programme concret : Gestion simple de véhicules
class Vehicule:
    """
    Classe générique pour un véhicule.
    """
    
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def demarrer(self):
        return "Le véhicule démarre."

class Voiture(Vehicule):
    def demarrer(self):
        return "La voiture démarre en tournant la clé."

class Moto(Vehicule):
    def demarrer(self):
        return "La moto démarre en appuyant sur le bouton d'allumage."

voiture1 = Voiture("Toyota", "Corolla", 2020)
moto1 = Moto("Honda", "CB500F", 2019)

print(voiture1.demarrer())
print(moto1.demarrer())
