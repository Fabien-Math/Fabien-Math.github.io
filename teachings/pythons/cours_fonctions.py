# Les fonctions en python

print("Fonction simple")

def dire_bonjour():
    print("bonjour !")

dire_bonjour()
input()












print("\nFonction avec parametre")

def dire_bonjour_a(nom):
    print("bonjour", nom)

dire_bonjour_a("alice")
dire_bonjour_a("bob")
input()












print("\nFonction avec plusieurs parametres")

def additionner(a, b):
    print(a + b)

additionner(10, 5)
input()












print("\nFonction avec return")

def additionner(a, b):
    return a + b

resultat = additionner(10, 5)

print("resultat :", resultat)
input()













print("\nPlusieurs valeurs")

def calculer(a, b):
    somme = a + b
    produit = a * b
    return somme, produit

somme, produit = calculer(10, 5)

print("somme :", somme)
print("produit :", produit)
input()











print("\nParametre par defaut")

def saluer(nom="ami"):
    print("bonjour", nom)

saluer()
saluer("alice")
input()












print("\nArguments nommes ")

def presenter(nom, age):
    print("nom :", nom)
    print("age :", age)

presenter(age=20, nom="alice")
input()











print("\n*args ")

def additionner_tout(*nombres):
    total = 0

    for nombre in nombres:
        total += nombre

    return total

print(additionner_tout(1, 2, 3))
print(additionner_tout(10, 20, 30, 40))
input()












print("\n**kwargs ")

def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(cle, ":", valeur)

afficher_infos(
    nom="alice",
    age=20,
    ville="paris"
)
input()












print("\nFonction lambda ")

carre = lambda x: x ** 2

print("carre de 5 :", carre(5))
input()












print("\nFonction dans une fonction ")

def fonction_exterieure():
    
    def fonction_interieure():
        print("bonjour depuis la fonction interieure")

    fonction_interieure()

fonction_exterieure()
input()












print("\nPortee des variables ")

variable_globale = "je suis globale"

def tester_portee():
    variable_locale = "je suis locale"

    print(variable_globale)
    print(variable_locale)

tester_portee()
input()












print("\nFonction recursive ")

def factorielle(n):

    if n == 0:
        return 1

    return n * factorielle(n - 1)

print("factorielle de 5 :", factorielle(5))
input()












print("\nFonction comme argument ")

def executer(fonction, valeur):
    return fonction(valeur)

def doubler(x):
    return x * 2

resultat = executer(doubler, 10)

print("resultat :", resultat)
input()



















# Minimal function
def foo():
    print("Do something")

# Complete function
def func(a, ao=None, aa:int=1, *args, **kwargs) -> str:
    """_summary_

    Args:
        a (_type_): _description_
        ao (_type_, optional): _description_. Defaults to None.
        aa (int, optional): _description_. Defaults to 1.

    Returns:
        str: _description_
    """
    print("Do something")
    return "Hello world!"