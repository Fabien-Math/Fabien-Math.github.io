---
layout: page
title: Python - Opérateurs
permalink: /enseignement/python_scripts/cours_operateurs
toc:
  sidebar: right
---

[Fichier brut](/assets/codes/python/cours_operateurs.py)


## Operateurs arithmetiques
```python
a = 10
b = 3


print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)
```

## operateurs de comparaison
```python
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
```


## operateurs logiques
```python
x = True
y = False

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)
```


## operateurs d'affectation
```python
n = 10

print("n =", n)

n += 5
print("n += 5  ->", n)

n -= 3
print("n -= 3  ->", n)

n *= 2
print("n *= 2  ->", n)

n /= 4
print("n /= 4  ->", n)

n //= 2
print("n //= 2 ->", n)

n %= 3
print("n %= 3  ->", n)

n **= 2
print("n **= 2 ->", n)
```


## operateurs bit a bit
```python
a = 10
b = 3

print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~a     =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
```


## operateurs d'appartenance
```python
liste = [1, 2, 3, 4, 5]

print("3 in liste      :", 3 in liste)
print("10 in liste     :", 10 in liste)
print("10 not in liste :", 10 not in liste)
```


## operateurs d'identite
```python
objet1 = [1, 2, 3]
objet2 = objet1
objet3 = [1, 2, 3]

print("objet1 is objet2     :", objet1 is objet2)
print("objet1 is objet3     :", objet1 is objet3)
print("objet1 is not objet3 :", objet1 is not objet3)
```


## operateurs avec des chaines
```python
prenom = "alice"
nom = "dupont"

print("concatenation :", prenom + " " + nom)
print("repetition    :", prenom * 3)
print("alice" in prenom)
print("bob" not in prenom)
```


## operateur ternaire
```python
age = 20
message = "majeur" if age >= 18 else "mineur"

print(message)
```
## operateur walrus :=
```python
if (longueur := len("python")) > 5:
    print("Le mot contient", longueur, "caracteres.")
```