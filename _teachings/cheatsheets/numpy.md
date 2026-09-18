---
layout: page
title: Python — NumPy
permalink: /enseignement/cheatsheets/python/numpy
toc:
  sidebar: right
---


| Catégorie     | Fonction / objet      | Exemple                       | Description                                            |
| ------------- | --------------------- | ----------------------------- | ------------------------------------------------------ |
| Import        | `np`                  | `import numpy as np`          | Convention courante pour importer NumPy                |
| Tableau       | `np.ndarray`          | `np.array([1, 2, 3])`         | Structure principale de NumPy pour stocker des données |
| Création      | `np.array()`          | `np.array([1, 2, 3])`         | Crée un tableau NumPy                                  |
| Création      | `np.zeros()`          | `np.zeros(5)`                 | Crée un tableau rempli de zéros                        |
| Création      | `np.ones()`           | `np.ones(5)`                  | Crée un tableau rempli de uns                          |
| Création      | `np.empty()`          | `np.empty(5)`                 | Crée un tableau sans initialiser ses valeurs           |
| Création      | `np.full()`           | `np.full(5, 10)`              | Crée un tableau rempli d'une valeur                    |
| Création      | `np.arange()`         | `np.arange(0, 10, 2)`         | Crée une suite de valeurs avec un pas                  |
| Création      | `np.linspace()`       | `np.linspace(0, 1, 5)`        | Crée des valeurs régulièrement espacées                |
| Aléatoire     | `np.random.rand()`    | `np.random.rand(5)`           | Génère des nombres flottants aléatoires entre 0 et 1   |
| Aléatoire     | `np.random.randint()` | `np.random.randint(1, 10, 5)` | Génère des entiers aléatoires                          |
| Aléatoire     | `np.random.randn()`   | `np.random.randn(5)`          | Génère des valeurs selon une loi normale               |
| Dimensions    | `.ndim`               | `array.ndim`                  | Nombre de dimensions du tableau                        |
| Dimensions    | `.shape`              | `array.shape`                 | Taille de chaque dimension                             |
| Dimensions    | `.size`               | `array.size`                  | Nombre total d'éléments                                |
| Type          | `.dtype`              | `array.dtype`                 | Type des données du tableau                            |
| Taille        | `.itemsize`           | `array.itemsize`              | Taille en octets d'un élément                          |
| Indexation    | `[]`                  | `array[0]`                    | Accède à un élément                                    |
| Slicing       | `[:]`                 | `array[1:4]`                  | Extrait une partie du tableau                          |
| 2D            | `[ligne, colonne]`    | `array[1, 2]`                 | Accède à un élément d'un tableau 2D                    |
| Ligne         | `:`                   | `array[0, :]`                 | Sélectionne une ligne                                  |
| Colonne       | `:`                   | `array[:, 0]`                 | Sélectionne une colonne                                |
| Reshape       | `.reshape()`          | `array.reshape(2, 3)`         | Change la forme du tableau                             |
| Aplatir       | `.flatten()`          | `array.flatten()`             | Transforme le tableau en une dimension                 |
| Transposition | `.T`                  | `array.T`                     | Inverse les axes d'un tableau 2D                       |
| Copie         | `.copy()`             | `array.copy()`                | Crée une copie indépendante                            |
| Concaténation | `np.concatenate()`    | `np.concatenate([a, b])`      | Assemble plusieurs tableaux                            |
| Empilement    | `np.vstack()`         | `np.vstack([a, b])`           | Empile verticalement                                   |
| Empilement    | `np.hstack()`         | `np.hstack([a, b])`           | Empile horizontalement                                 |
| Calcul        | `np.sum()`            | `np.sum(array)`               | Calcule la somme                                       |
| Calcul        | `np.prod()`           | `np.prod(array)`              | Calcule le produit                                     |
| Statistique   | `np.mean()`           | `np.mean(array)`              | Calcule la moyenne                                     |
| Statistique   | `np.median()`         | `np.median(array)`            | Calcule la médiane                                     |
| Statistique   | `np.std()`            | `np.std(array)`               | Calcule l'écart-type                                   |
| Statistique   | `np.var()`            | `np.var(array)`               | Calcule la variance                                    |
| Statistique   | `np.min()`            | `np.min(array)`               | Trouve la valeur minimale                              |
| Statistique   | `np.max()`            | `np.max(array)`               | Trouve la valeur maximale                              |
| Statistique   | `np.argmin()`         | `np.argmin(array)`            | Retourne l'index du minimum                            |
| Statistique   | `np.argmax()`         | `np.argmax(array)`            | Retourne l'index du maximum                            |
| Mathématique  | `np.sqrt()`           | `np.sqrt(array)`              | Calcule la racine carrée                               |
| Mathématique  | `np.abs()`            | `np.abs(array)`               | Calcule la valeur absolue                              |
| Mathématique  | `np.power()`          | `np.power(array, 2)`          | Élève les valeurs à une puissance                      |
| Mathématique  | `np.exp()`            | `np.exp(array)`               | Calcule l'exponentielle                                |
| Mathématique  | `np.log()`            | `np.log(array)`               | Calcule le logarithme naturel                          |
| Mathématique  | `np.sin()`            | `np.sin(array)`               | Calcule le sinus                                       |
| Mathématique  | `np.cos()`            | `np.cos(array)`               | Calcule le cosinus                                     |
| Comparaison   | `>`                   | `array > 10`                  | Compare chaque élément à une valeur                    |
| Comparaison   | `<`                   | `array < 10`                  | Compare chaque élément à une valeur                    |
| Comparaison   | `==`                  | `array == 10`                 | Teste l'égalité élément par élément                    |
| Filtrage      | Masque booléen        | `array[array > 10]`           | Sélectionne les valeurs respectant une condition       |
| Remplacement  | Masque booléen        | `array[array > 10] = 0`       | Modifie les valeurs respectant une condition           |
| Condition     | `np.where()`          | `np.where(array > 10, 1, 0)`  | Choisit une valeur selon une condition                 |
| Recherche     | `np.unique()`         | `np.unique(array)`            | Retourne les valeurs uniques                           |
| Recherche     | `np.sort()`           | `np.sort(array)`              | Retourne les valeurs triées                            |
| Recherche     | `np.argsort()`        | `np.argsort(array)`           | Retourne les indices du tri                            |
| Linéaire      | `@`                   | `A @ B`                       | Effectue un produit matriciel                          |
| Linéaire      | `np.dot()`            | `np.dot(A, B)`                | Effectue un produit scalaire ou matriciel              |
| Linéaire      | `np.linalg.inv()`     | `np.linalg.inv(A)`            | Calcule l'inverse d'une matrice                        |
| Linéaire      | `np.linalg.det()`     | `np.linalg.det(A)`            | Calcule le déterminant                                 |
| Linéaire      | `np.linalg.solve()`   | `np.linalg.solve(A, b)`       | Résout un système d'équations linéaires                |
| Type          | `.astype()`           | `array.astype(float)`         | Convertit le type des éléments                         |
| Arrondi       | `np.round()`          | `np.round(array, 2)`          | Arrondit les valeurs                                   |
| Arrondi       | `np.floor()`          | `np.floor(array)`             | Arrondit vers le bas                                   |
| Arrondi       | `np.ceil()`           | `np.ceil(array)`              | Arrondit vers le haut                                  |
| Valeur        | `np.clip()`           | `np.clip(array, 0, 10)`       | Limite les valeurs entre deux bornes                   |
| Vérification  | `np.isnan()`          | `np.isnan(array)`             | Détecte les valeurs `NaN`                              |
| Vérification  | `np.isinf()`          | `np.isinf(array)`             | Détecte les valeurs infinies                           |

