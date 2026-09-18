---
layout: page
title: Python - Dictionnaires
permalink: /enseignement/python_scripts/cours_dictionnaires
toc:
  sidebar: right
---

[Fichier brut](/assets/codes/python/cours_dictionnaires.py)

## Creation d'un dictionnaire

```python
print("Creation d'un dictionnaire")
personne = {
    "nom": "alice",
    "age": 20,
    "ville": "Toulon"
}
print("Dictionnaire :", personne)
input()
```

## Acceder aux valeurs
```python
print("Acceder aux valeurs")
print("Nom :", personne["nom"])
print("Age :", personne["age"])
print("Ville :", personne["ville"])
input()
```

## Modifier une valeur
```python
print("Modifier une valeur")
print("Avant modification :", personne)

personne["age"] = 21

print("Apres modification :", personne)
input()
```

## Ajouter une nouvelle valeur
```python
print("Ajouter une nouvelle valeur")
print("Avant ajout :", personne)

personne["metier"] = "developpeur"

print("Apres ajout :", personne)
input()
```

## Taille du dictionnaire
```python
print("Taille du dictionnaire")
print("Nombre d'elements :", len(personne))
input()
```

## Verifier si une cle existe
```python
print("Verifier si une cle existe")
print("nom" in personne)
print("email" in personne)
input()
```

## Obtenir une valeur avec get()
```python
print("Obtenir une valeur avec get()")
print("Nom :", personne.get("nom"))
print("Email :", personne.get("email"))
print("Email :", personne.get("email", "nom.prenom@mail.fr"))
input()
```

## Parcourir les cles
```python
print("Parcourir les cles")
print("Cles du dictionnaire :")

for cle in personne:
    print(cle)

input()
```

## Parcourir les valeurs
```python
print("Parcourir les valeurs")
print("Valeurs du dictionnaire :")

for valeur in personne.values():
    print(valeur)

input()
```

## Parcourir les cles et les valeurs
```python
print("Parcourir les cles et les valeurs")
print("Cles et valeurs :")

for cle, valeur in personne.items():
    print(cle, ":", valeur)

input()
```

## Supprimer un element
```python
print("Supprimer un element")
print("Avant suppression :", personne)

del personne["ville"]

print("Apres suppression :", personne)
input()
```

## Supprimer avec pop()
```python
print("Supprimer avec pop()")
personne["ville"] = "Toulon" # Cette ligne reintroduit la cle "ville" avec la valeur "Toulon"
print("Avant pop() :", personne)

age = personne.pop("age")

print("Age supprime :", age)
print("Apres pop() :", personne)
input()
```

## Vider le dictionnaire
```python
print("Vider le dictionnaire")
personne.clear()

print("Dictionnaire apres clear() :", personne)
input()
```

## QUESTION
```python
print("QUESTION")
personne = {
    "nom": "alice",
    "age": 20,
    "ville": "Toulon"
}
personne_bis = personne
print("Avant modification de personne:", personne)
print("Avant modification de personne_bis:", personne_bis)

personne_bis["nom"] = "Bob"

print("\nApres modification de personne_bis:", personne_bis)
input()
print("Apres modification de personne:", personne)
print("La liste personne a change, pourquoi ?")
```

### Maniere de creer des dictionnaires en python

## Creation d'un dictionnaire classique
```python
print("Creation d'un dictionnaire classique")
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Toulon"
}
print(personne)
input()
```

## Creation d'un dictionnaire vide (Initialisation)
```python
print("Creation d'un dictionnaire vide (Initialisation)")
personne = {}
print(personne)
input()
```

## Creation d'un dictionnaire avec dict
```python
print("Creation d'un dictionnaire avec dict")
personne = dict(
    nom="Alice",
    age=25,
    ville="Toulon"
)
print(personne)
input()
```

## Creation d'un dictionnaire a partir d'une liste de tuples
```python
print("Creation d'un dictionnaire a partir d'une liste de tuples")
donnees = [
    ("nom", "Alice"),
    ("age", 25),
    ("ville", "Toulon")
]

personne = dict(donnees)
print(personne)
input()
```

## Creation d'un dictionnaire avec des cles et des valeurs
```python
print("Creation d'un dictionnaire avec des cles et des valeurs")
cles = ["nom", "age", "ville"]
valeurs = ["Alice", 25, "Toulon"]

personne = dict(zip(cles, valeurs))
print(personne)
input()
```

## Creation d'un dictionnaire avec une comprehension
```python
print("Creation d'un dictionnaire avec une comprehension")
carres = {
    x: x ** 2
    for x in range(10)
}
print(carres)
input()
```

## Creation d'un dictionnaire avec une condition
```python
print("Creation d'un dictionnaire avec une condition")
pairs = {
    x: x ** 2
    for x in range(20)
    if x % 2 == 0
}
print(pairs)
input()
```

## Creation d'un dictionnaire a partir d'une liste
```python
print("Creation d'un dictionnaire a partir d'une liste")
nombres = [1, 2, 3, 4, 5]

carres = {
    nombre: nombre ** 2
    for nombre in nombres
}
print(carres)
input()
```

## Creation d'un dictionnaire avec une fonction
```python
print("Creation d'un dictionnaire avec une fonction")
def foo(x):
    return x ** 2

donnees = range(10)

resultat = {
    x: foo(x)
    for x in donnees
}

print(resultat)
input()
```

## Creation d'un dictionnaire imbrique
```python
print("Creation d'un dictionnaire imbrique")
personne = {
    "nom": "Alice",
    "age": 25,
    "adresse": {
        "ville": "Toulon",
        "code_postal": 75000
    }
}

print(personne)
input()
```

## Creation d'un dictionnaire contenant des listes
```python
print("Creation d'un dictionnaire contenant des listes")
classe = {
    "nom": "Python",
    "eleves": ["Alice", "Bob", "Charlie"],
    "notes": [15, 12, 18]
}

print(classe)
input()
```

## Copie d'un dictionnaire
```python
print("Copie d'un dictionnaire")
personne = {
    "nom": "Alice",
    "age": 25
}

copie = personne.copy()

print(personne)
print(copie)
input()
```

## Creation d'un dictionnaire avec des valeurs identiques
```python
print("Creation d'un dictionnaire avec des valeurs identiques")
cles = ["a", "b", "c", "d"]

resultat = dict.fromkeys(cles, 0)

print(resultat)
```