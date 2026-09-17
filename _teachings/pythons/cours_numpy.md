---
layout: page
title: Python - Numpy
permalink: /enseignement/python_scripts/cours_numpy
toc:
  sidebar: right
---

```python
import numpy as np
```

## Creation d'un tableau
```python
print("Creation d'un tableau")
numbers = np.array([1, 2, 3, 4, 5])
print(numbers)
```

## Tableau 2D
```python
print("Tableau 2D")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix)
```

## Tableau rempli de zeros
```python
print("Tableau rempli de zeros")
zeros = np.zeros(5)
print(zeros)
```


## Tableau rempli de uns
```python
print("Tableau rempli de uns")
ones = np.ones(5)
print(ones)
```


## Tableau avec une suite de nombres
```python
print("Tableau avec une suite de nombres")
numbers = np.arange(0, 10, 2)
print(numbers)
```


## Tableau avec des valeurs espacees regulierement
```python
print("Tableau avec des valeurs espacees regulierement")
numbers = np.linspace(0, 1, 5)
print(numbers)
```

## Dimensions d'un tableau
```python
print("Dimensions d'un tableau")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
```


## Acceder aux elements
```python
print("Acceder aux elements")
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
```


## Acceder aux elements d'une matrice
```python
print("Acceder aux elements d'une matrice")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[0, 0])
print(matrix[1, 2])
print(matrix[:, 0])
print(matrix[0, :])
```


## Modifier un element
```python
print("Modifier un element")
numbers = np.array([1, 2, 3, 4, 5])
numbers[0] = 100
print(numbers)
```


## Operations mathematiques
```python
print("Operations mathematiques")
numbers = np.array([1, 2, 3, 4, 5])
print(numbers + 10)
print(numbers * 2)
print(numbers ** 2)
```



## Operations entre tableaux
```python
print("Operations entre tableaux")
numbers_a = np.array([1, 2, 3])
numbers_b = np.array([4, 5, 6])
print(numbers_a + numbers_b)
print(numbers_a * numbers_b)
```



## Fonctions mathematiques
```python
print("Fonctions mathematiques")
numbers = np.array([1, 4, 9, 16])
print(np.sqrt(numbers))
print(np.power(numbers, 2))
print(np.abs([-10, -5, 0, 5, 10]))
```



## Statistiques
```python
print("Statistiques")
numbers = np.array([10, 20, 30, 40, 50])
print(np.sum(numbers))
print(np.mean(numbers))
print(np.median(numbers))
print(np.min(numbers))
print(np.max(numbers))
print(np.std(numbers))
```



## Somme par ligne et par colonne
```python
print("Somme par ligne et par colonne")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(np.sum(matrix))
print(np.sum(matrix, axis=0))
print(np.sum(matrix, axis=1))
```



## Comparaisons
```python
print("Comparaisons")
numbers = np.array([1, 5, 10, 15, 20])
print(numbers > 10)
print(numbers == 10)
print(numbers != 10)
```



## Filtrer un tableau
```python
print("Filtrer un tableau")
numbers = np.array([1, 5, 10, 15, 20])
filtered = numbers[numbers > 10]
print(filtered)
```

## Plusieurs conditions
```python
print("Plusieurs conditions")
numbers = np.array([1, 5, 10, 15, 20, 25])
filtered = numbers[(numbers > 5) & (numbers < 20)]
print(filtered)
```


## Remplacer des valeurs
```python
print("Remplacer des valeurs")
numbers = np.array([1, 2, 3, 4, 5])
numbers[numbers > 3] = 0
print(numbers)
```


## Reshape
```python
print("Reshape")
numbers = np.arange(1, 10)
matrix = numbers.reshape(3, 3)
print(matrix)
```


## Aplatir un tableau
```python
print("Aplatir un tableau")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
numbers = matrix.flatten()
print(numbers)
```


## Transposer une matrice
```python
print("Transposer une matrice")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix.T)
```



## Concatener des tableaux
```python
print("Concatener des tableaux")
numbers_a = np.array([1, 2, 3])
numbers_b = np.array([4, 5, 6])
numbers = np.concatenate([numbers_a, numbers_b])
print(numbers)
```


## Generer des nombres aleatoires
```python
print("Generer des nombres aleatoires")
numbers = np.random.rand(5)
print(numbers)
```




## Entiers aleatoires
```python
print("Entiers aleatoires")
numbers = np.random.randint(1, 100, 10)
print(numbers)
```


## Matrice aleatoire
```python
print("Matrice aleatoire")
matrix = np.random.randint(1, 10, (3, 3))
print(matrix)
```


## Melanger un tableau
```python
print("Melanger un tableau")
numbers = np.array([1, 2, 3, 4, 5])
np.random.shuffle(numbers)
print(numbers)
```



## Produit matriciel
```python
print("Produit matriciel")
matrix_a = np.array([
    [1, 2],
    [3, 4]
])
matrix_b = np.array([
    [5, 6],
    [7, 8]
])
result = matrix_a @ matrix_b
print(result)
```



## Inverse d'une matrice
```python
print("Inverse d'une matrice")
matrix = np.array([
    [1, 2],
    [3, 4]
])
inverse = np.linalg.inv(matrix)
print(inverse)
```


## Resolution d'un systeme lineaire
```python
print("Resolution d'un systeme lineaire")
matrix = np.array([
    [2, 1],
    [1, 3]
])
values = np.array([5, 7])
solution = np.linalg.solve(matrix, values)
print(solution)
```