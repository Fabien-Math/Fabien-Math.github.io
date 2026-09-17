---
layout: page
title: Python - Structures
permalink: /enseignement/python_scripts/cours_structures
toc:
  sidebar: left
---


## Conditions : if / else
```python
nombre = 10
print("Nombre :", nombre)
if nombre > 0:
    print("Le nombre est positif")
else:
    print("Le nombre est négatif ou nul")


note = 14
print("\nNote :", note)
if note >= 16:
    print("Mention Très bien")
elif note >= 10:
    print("Validé")
elif note >= 10 and not note%2:
    print("Validé pair")
else:
    print("Non validé")
```


## Boucle for
```python
print("\nBoucle for :")
for i in range(5):
    print("i =", i)

nombres = [10, 20, 30, 40]
print("\nParcours de la liste :")
for nombre in nombres:
    print(nombre)
```


## Boucle while
```python
print("\nBoucle while :")
x = 0
while x < 5:
    print("x =", x)
    x = x + 1
```


## Debug
```python
print("\nObserver l'exécution :")
x = 0
while x < 3:
    print("DEBUG - début : x =", x)
    x = x + 1
    print("DEBUG - fin   : x =", x)
```