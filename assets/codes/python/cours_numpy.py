# Module Numpy
import numpy as np


# Creation d'un tableau
print("Creation d'un tableau")
numbers = np.array([1, 2, 3, 4, 5])
print(numbers)
input()





# Tableau 2D
print("Tableau 2D")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix)
input()





# Tableau rempli de zeros
print("Tableau rempli de zeros")
zeros = np.zeros(5)
print(zeros)
input()






# Tableau rempli de uns
print("Tableau rempli de uns")
ones = np.ones(5)
print(ones)
input()






# Tableau avec une suite de nombres
print("Tableau avec une suite de nombres")
numbers = np.arange(0, 10, 2)
print(numbers)
input()






# Tableau avec des valeurs espacees regulierement
print("Tableau avec des valeurs espacees regulierement")
numbers = np.linspace(0, 1, 5)
print(numbers)
input()





# Dimensions d'un tableau
print("Dimensions d'un tableau")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
input()









# Acceder aux elements
print("Acceder aux elements")
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
input()









# Acceder aux elements d'une matrice
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
input()






# Modifier un element
print("Modifier un element")
numbers = np.array([1, 2, 3, 4, 5])
numbers[0] = 100
print(numbers)
input()






# Operations mathematiques
print("Operations mathematiques")
numbers = np.array([1, 2, 3, 4, 5])
print(numbers + 10)
print(numbers * 2)
print(numbers ** 2)
input()







# Operations entre tableaux
print("Operations entre tableaux")
numbers_a = np.array([1, 2, 3])
numbers_b = np.array([4, 5, 6])
print(numbers_a + numbers_b)
print(numbers_a * numbers_b)
input()







# Fonctions mathematiques
print("Fonctions mathematiques")
numbers = np.array([1, 4, 9, 16])
print(np.sqrt(numbers))
print(np.power(numbers, 2))
print(np.abs([-10, -5, 0, 5, 10]))
input()







# Statistiques
print("Statistiques")
numbers = np.array([10, 20, 30, 40, 50])
print(np.sum(numbers))
print(np.mean(numbers))
print(np.median(numbers))
print(np.min(numbers))
print(np.max(numbers))
print(np.std(numbers))
input()







# Somme par ligne et par colonne
print("Somme par ligne et par colonne")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(np.sum(matrix))
print(np.sum(matrix, axis=0))
print(np.sum(matrix, axis=1))
input()







# Comparaisons
print("Comparaisons")
numbers = np.array([1, 5, 10, 15, 20])
print(numbers > 10)
print(numbers == 10)
print(numbers != 10)
input()







# Filtrer un tableau
print("Filtrer un tableau")
numbers = np.array([1, 5, 10, 15, 20])
filtered = numbers[numbers > 10]
print(filtered)
input()





# Plusieurs conditions
print("Plusieurs conditions")
numbers = np.array([1, 5, 10, 15, 20, 25])
filtered = numbers[(numbers > 5) & (numbers < 20)]
print(filtered)
input()






# Remplacer des valeurs
print("Remplacer des valeurs")
numbers = np.array([1, 2, 3, 4, 5])
numbers[numbers > 3] = 0
print(numbers)
input()






# Reshape
print("Reshape")
numbers = np.arange(1, 10)
matrix = numbers.reshape(3, 3)
print(matrix)
input()






# Aplatir un tableau
print("Aplatir un tableau")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
numbers = matrix.flatten()
print(numbers)
input()






# Transposer une matrice
print("Transposer une matrice")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix.T)
input()







# Concatener des tableaux
print("Concatener des tableaux")
numbers_a = np.array([1, 2, 3])
numbers_b = np.array([4, 5, 6])
numbers = np.concatenate([numbers_a, numbers_b])
print(numbers)
input()






# Generer des nombres aleatoires
print("Generer des nombres aleatoires")
numbers = np.random.rand(5)
print(numbers)
input()








# Entiers aleatoires
print("Entiers aleatoires")
numbers = np.random.randint(1, 100, 10)
print(numbers)
input()






# Matrice aleatoire
print("Matrice aleatoire")
matrix = np.random.randint(1, 10, (3, 3))
print(matrix)
input()






# Melanger un tableau
print("Melanger un tableau")
numbers = np.array([1, 2, 3, 4, 5])
np.random.shuffle(numbers)
print(numbers)
input()







# Produit matriciel
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
input()







# Inverse d'une matrice
print("Inverse d'une matrice")
matrix = np.array([
    [1, 2],
    [3, 4]
])
inverse = np.linalg.inv(matrix)
print(inverse)
input()







# Resolution d'un systeme lineaire
print("Resolution d'un systeme lineaire")
matrix = np.array([
    [2, 1],
    [1, 3]
])
values = np.array([5, 7])
solution = np.linalg.solve(matrix, values)
print(solution)
