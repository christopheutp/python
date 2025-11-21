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
