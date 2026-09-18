# Les listes en python

# Creation d'une liste
print("Creation d'une liste")
nombres = [10, 20, 30, 40, 50, 60]
# nombres = [10, 20, 30, "eheh"]
print("Liste :", nombres)
input()

# Acceder aux elements
print("Acceder aux elements")
print("Premier element :", nombres[0])
print("Deuxieme element :", nombres[1])
print("Dernier element :", nombres[-1])
print("Trois premiers elements :", nombres[:3])
print("Trois derniers elements :", nombres[3:])
print("Deux elements entre l'indice 1 et 2 :", nombres[1:3])
input()

# Modifier un element
print("Modifier un element")
print("Avant modification :", nombres)
nombres[1] = 99
print("Apres modification :", nombres)
input()

# Ajouter un element
print("Ajouter un element")
print("Avant ajout :", nombres)
nombres.append(50)
print("Apres ajout :", nombres)
input()

# Taille de la liste
print("Taille de la liste")
print("Nombre d'elements :", len(nombres))
input()

# Parcourir la liste
print("Parcourir la liste")
print("Parcours de la liste :")
for nombre in nombres:
    print(nombre)
input()

# Parcourir avec les indices
print("Parcourir avec les indices")
print("Indices et valeurs :")
for i in range(len(nombres)):
    print("Indice", i, ":", nombres[i])
input()

# Supprimer un element
print("Supprimer un element")
print("Avant suppression :", nombres)
nombres.remove(30)
print("Apres suppression :", nombres)
input()

# QUESTION
nombres_bis = nombres
print("Avant modification de nombres:", nombres)
print("Avant modification de nombres_bis:", nombres_bis)

nombres_bis[1] = 17

print("\nApres modification de nombres_bis:", nombres_bis)
input()
print("Apres modification de nombres:", nombres)
print("La liste nombres a change, pourquoi ?")








### Maniere de creer des listes en python
# Creation d'une liste classique
print("Creation d'une liste classique")
liste = [1, 2, 3]
print(liste)
input()


# Creation d'une liste vide
print("Creation d'une liste vide")
liste = []
print(liste)
input()


# Creation d'une liste avec range
print("Creation d'une liste avec range")
liste = list(range(10))
print(liste)
input()


# Transformation d'une chaine en liste
print("Transformation d'une chaine en liste")
liste = list("Python")
print(liste)
input()


# Creation d'une liste avec une comprehension
print("Creation d'une liste avec une comprehension")
liste = [x ** 2 for x in range(10)]
print(liste)
input()


# Creation d'une liste avec une comprehension depuis plusieurs liste
print("Creation d'une liste avec une comprehension depuis plusieurs liste")
prenoms = ["Alice", "Bob", "Charlie"]
villes = ["Toulon", "La Garde", "Le Pradet"]
liste = [(prenom, ville) for prenom, ville in zip(prenoms, villes)]
print(liste)
input()


# Creation d'une liste avec une condition
print("Creation d'une liste avec une condition")
liste = [x for x in range(20) if x % 2 == 0]
print(liste)
input()


# Creation d'une liste avec une fonction
print("Creation d'une liste avec une fonction")
def foo(x):
    return x**2

donnees = list(range(10))
liste = [foo(x) for x in donnees]
print(liste)
input()


# Transformation d'une matrice en une seule liste
print("Transformation d'une matrice en une seule liste")
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

liste = [x for ligne in matrice for x in ligne]
print(liste)
print(matrice[0])
print(matrice[0][2])
input()


# Copie d'une liste
print("Copie d'une liste")
copie = liste.copy()
copie.append(100)
print(liste)
print(copie)
