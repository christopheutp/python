# Ce module contient quelques fonctions simples et une variable globale.

def saluer(nom):
    """Retourne un message de salutation avec le nom donné."""
    return f"Bonjour, {nom} !"

VERSION = "1.0"

def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b

if __name__ == "__main__":
    print(__name__)
    print("Je suis un print dans mon_module.py")
    print(addition(5,5))
    print(saluer("toto"))

    