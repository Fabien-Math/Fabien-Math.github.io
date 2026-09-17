---
layout: page
title: Python - Listes
permalink: /enseignement/python_scripts/cours_listes
toc:
  sidebar: right
---


# Les listes en python

## Creation d'une liste
```python
print("Creation d'une liste")
nombres = [10, 20, 30, 40, 50, 60]
# nombres = [10, 20, 30, "eheh"]
print("Liste :", nombres)
```

## Acceder aux elements
```python
print("Acceder aux elements")
print("Premier element :", nombres[0])
print("Deuxieme element :", nombres[1])
print("Dernier element :", nombres[-1])
print("Trois premiers elements :", nombres[:3])
print("Trois derniers elements :", nombres[3:])
print("Deux elements entre l'indice 1 et 2 :", nombres[1:3])
```

## Modifier un element
```python
print("Modifier un element")
print("Avant modification :", nombres)
nombres[1] = 99
print("Apres modification :", nombres)
```

## Ajouter un element
```python
print("Ajouter un element")
print("Avant ajout :", nombres)
nombres.append(50)
print("Apres ajout :", nombres)
```

## Taille de la liste
```python
print("Taille de la liste")
print("Nombre d'elements :", len(nombres))
```

## Parcourir la liste
```python
print("Parcourir la liste")
print("Parcours de la liste :")
for nombre in nombres:
    print(nombre)
```

## Parcourir avec les indices
```python
print("Parcourir avec les indices")
print("Indices et valeurs :")
for i in range(len(nombres)):
    print("Indice", i, ":", nombres[i])
```

## Supprimer un element
```python
print("Supprimer un element")
print("Avant suppression :", nombres)
nombres.remove(30)
print("Apres suppression :", nombres)
```

### QUESTION
```python
nombres_bis = nombres
print("Avant modification de nombres:", nombres)
print("Avant modification de nombres_bis:", nombres_bis)

nombres_bis[1] = 17

print("\nApres modification de nombres_bis:", nombres_bis)
print("Apres modification de nombres:", nombres)
print("La liste nombres a change, pourquoi ?")
```








### Maniere de creer des listes en python
## Creation d'une liste classique
```python
print("Creation d'une liste classique")
liste = [1, 2, 3]
print(liste)
```


## Creation d'une liste vide
```python
print("Creation d'une liste vide")
liste = []
print(liste)
```


## Creation d'une liste avec range
```python
print("Creation d'une liste avec range")
liste = list(range(10))
print(liste)
```


## Transformation d'une chaine en liste
```python
print("Transformation d'une chaine en liste")
liste = list("Python")
print(liste)
```


## Creation d'une liste avec une comprehension
```python
print("Creation d'une liste avec une comprehension")
liste = [x ** 2 for x in range(10)]
print(liste)
```


## Creation d'une liste avec une comprehension depuis plusieurs liste
```python
print("Creation d'une liste avec une comprehension depuis plusieurs liste")
prenoms = ["Alice", "Bob", "Charlie"]
villes = ["Toulon", "La Garde", "Le Pradet"]
liste = [(prenom, ville) for prenom, ville in zip(prenoms, villes)]
print(liste)
```


## Creation d'une liste avec une condition
```python
print("Creation d'une liste avec une condition")
liste = [x for x in range(20) if x % 2 == 0]
print(liste)
```


## Creation d'une liste avec une fonction
```python
print("Creation d'une liste avec une fonction")
def foo(x):
    return x**2

donnees = list(range(10))
liste = [foo(x) for x in donnees]
print(liste)
```


## Transformation d'une matrice en une seule liste
```python
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
```


## Copie d'une liste
```python
print("Copie d'une liste")
copie = liste.copy()
copie.append(100)
print(liste)
print(copie)
```