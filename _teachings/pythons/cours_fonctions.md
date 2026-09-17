---
layout: page
title: Python - Fonctions
permalink: /enseignement/python_scripts/cours_fonctions
toc:
  sidebar: left
---

# Les fonctions en python


#### Fonction simple
```python
def dire_bonjour():
    print("bonjour !")

dire_bonjour()
```


#### Fonction avec parametre
```python

def dire_bonjour_a(nom):
    print("bonjour", nom)

dire_bonjour_a("alice")
dire_bonjour_a("bob")
```


#### Fonction avec plusieurs parametres
```python

def additionner(a, b):
    print(a + b)

additionner(10, 5)
```


#### Fonction avec return
```python

def additionner(a, b):
    return a + b

resultat = additionner(10, 5)

print("resultat :", resultat)
```



#### Plusieurs valeurs
```python

def calculer(a, b):
    somme = a + b
    produit = a * b
    return somme, produit

somme, produit = calculer(10, 5)

print("somme :", somme)
print("produit :", produit)
```

#### Parametre par defaut
```python

def saluer(nom="ami"):
    print("bonjour", nom)

saluer()
saluer("alice")
```


#### Arguments nommes 
```python

def presenter(nom, age):
    print("nom :", nom)
    print("age :", age)

presenter(age=20, nom="alice")
```

#### *args 
```python

def additionner_tout(*nombres):
    total = 0

    for nombre in nombres:
        total += nombre

    return total

print(additionner_tout(1, 2, 3))
print(additionner_tout(10, 20, 30, 40))
```


#### **kwargs 
```python

def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(cle, ":", valeur)

afficher_infos(
    nom="alice",
    age=20,
    ville="paris"
)
```


#### Fonction lambda 
```python

carre = lambda x: x ** 2

print("carre de 5 :", carre(5))
```


#### Fonction dans une fonction 
```python

def fonction_exterieure():
    
    def fonction_interieure():
        print("bonjour depuis la fonction interieure")

    fonction_interieure()

fonction_exterieure()
```


#### Portee des variables 
```python

variable_globale = "je suis globale"

def tester_portee():
    variable_locale = "je suis locale"

    print(variable_globale)
    print(variable_locale)

tester_portee()
```

#### Fonction recursive 
```python

def factorielle(n):

    if n == 0:
        return 1

    return n * factorielle(n - 1)

print("factorielle de 5 :", factorielle(5))
```

#### Fonction comme argument 
```python

def executer(fonction, valeur):
    return fonction(valeur)

def doubler(x):
    return x * 2

resultat = executer(doubler, 10)

print("resultat :", resultat)
```







```python
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
```