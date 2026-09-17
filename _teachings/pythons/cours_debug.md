---
layout: page
title: Python - Outils de debug
permalink: /enseignement/python_scripts/cours_debug
toc:
  sidebar: right
---


```python
# Exemple
nombres = [12, -3, 8, 0, 15, -7, 10]

somme = 0
compteur = 0

for nombre in nombres:

    if nombre > 0:
        somme = somme + nombre

    compteur = compteur + 1

moyenne = somme / compteur

print("Moyenne des nombres positifs :", moyenne)


# Les outils pour du debug

# print()
print("Debug")


# type()
a = 10
b = 3.14
c = "Bonjour"
d = True

print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))
print(d, "->", type(d))


# help()
help(nombres.append)


# repr()
texte = "Bonjour\nPython"

print("Avec print :")
print(texte)

print("Avec repr :")
print(repr(texte))


# dir
print(dir(nombres))



# Exemple avec debug
valeurs = [12, -3, 8, 0, 15, -7, 10]

somme = 0
compteur = 0

for valeur in valeurs:

    print("\nValeur =", valeur)
    print("Avant :", somme, compteur)

    if valeur > 0:
        somme = somme + valeur

    compteur = compteur + 1

    print("Apres :", somme, compteur)


moyenne = somme / compteur

print("\nMoyenne =", moyenne)





# Exemple corrige
somme = 0
compteur = 0

for valeur in valeurs:

    if valeur > 0:

        somme = somme + valeur
        compteur = compteur + 1

        print("Valeur =", valeur)
        print("Somme =", somme)
        print("Compteur =", compteur)


moyenne = somme / compteur

print("\nMoyenne correcte =", moyenne)

```