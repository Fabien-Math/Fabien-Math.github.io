# Python

## L'Histoire de Python

Dans les années 70 et 80, les langages de programmation sont le C, C++, Fortran, Pascal, etc.

En 1989, *Python* est créé par Guido van Rossum

![Guido van Rossum](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Guido_van_Rossum_in_PyConUS24_%28cropped%29.jpg/250px-Guido_van_Rossum_in_PyConUS24_%28cropped%29.jpg)

Son objectif est de créer un langage :

- simple à lire
- agréable à programmer
- suffisamment puissant
- extensible
- permettant de produire rapidement des programmes.

En 1991, le langage est rendu public.

Programmation impérative structurée, fonctionnelle et orientée object.
Langage de haut niveau avec une synthaxe simple.

Multi plateforme :
Unix, MacOS, Windows, Android, iOS

En 2000, Python 2 est publié

En 2008, Python 3 est publié

### La force de Python:

```text
Python
  ├── NumPy       → calcul scientifique
  ├── SciPy       → mathématiques / ingénierie
  ├── Matplotlib  → visualisation
  ├── Pandas      → données
  ├── OpenCV      → vision
  ├── PyTorch     → intelligence artificielle
  └── ...
```

## Les types de données en Python

## Les operateurs en Python

## Les conditions et boucles

## Les listes

## Les fonctions

## Formatages

## Debug

## Convention de nommage

## Un premier programme

### Le shebang

```python
#! /usr/bin/env python
```

Le shebang indique au système quel interpréteur utiliser pour exécuter le script.

Il permet notamment d'exécuter directement le fichier comme un programme, à condition de lui donner les droits d'exécution :

```bash
chmod +x main.py
./main.py
```

### Définition d'une fonction principale

```python
def main():
    print("Do something")

if __name__ == "__main__":
    main()
```


### Exercice 1

[Exercice 1](Exercices/exercice_1.md)