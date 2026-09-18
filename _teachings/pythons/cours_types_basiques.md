---
layout: page
title: Python - Types basiques
permalink: /enseignement/python_scripts/cours_types_basiques
toc:
  sidebar: right
---

[Fichier brut](/assets/codes/python/cours_types_basiques.py)

## Entier — `int`
```python
age = 25
```

## Nombre réel — `float`
```python
temperature = 20.5
```

## Chaine de caractère — `str`
```python
nom = "Alice"
```

## Booléen — `bool`
```python
est_connecte = True
```

## Collection — `list`
```python
liste = [12, 15.6, 'e', print, complex(1, 2)]
```


print(type(age))
print(type(temperature))
print(type(nom))


## Le type détermine les opérations possibles sur une donnée
```python
3 + 2
"Bonjour" + 2
```


## Les variables: un nom associé à une valeur
```python
x = 10
x = x + 1 # Lit x, calcul x + 1 -> 11 puis stocke 11 dans x 

print(x)
```