---
layout: page
title: Python - Formatage
permalink: /enseignement/python/scripts/cours_formatages
toc:
  sidebar: right
---

[Fichier brut](/assets/codes/python/cours_formatages.py)


## Demonstration des f-strings en Python

```python
nom = "Alice"
age = 25
prix = 1234.5678
pourcentage = 0.8567
nombre = 42

print("Inserer une variable")
print(f"Bonjour {nom} !")
print(f"Tu as {age} ans.")
```

#### Calcul dans une f-string
```python
print(f"Dans 5 ans, tu auras {age + 5} ans.")
print(f"2 x 3 = {2 * 3}")
```

#### Nombres decimaux
```python
print(f"Prix : {prix:.2f}")          # 2 decimales
print(f"Prix : {prix:.1f}")          # 1 decimale
print(f"Prix : {prix:.0f}")          # Arrondi a l'entier
```
#### Pourcentages
```python
print(f"Progression : {pourcentage:.1%}")  # 85.7%
```

#### Separateur de milliers
```python
print(f"Nombre : {1234567:,}")        # 1,234,567
print(f"Nombre : {1234567:_}")        # 1_234_567
```

#### Largeur et alignement
```python
texte = "Python"

print(f"|{texte:<10}|")              # Aligne a gauche
print(f"|{texte:>10}|")              # Aligne a droite
print(f"|{texte:^10}|")              # Centre
```

#### Remplissage avec des caracteres
```python
print(f"|{texte:*<10}|")
print(f"|{texte:*>10}|")
print(f"|{texte:*^10}|")
```

#### Entiers avec des zeros
```python
print(f"Nombre : {nombre:05d}")       # 00042
```

#### Bases numeriques
```python
print(f"Decimal : {nombre:d}")
print(f"Binaire  : {nombre:b}")
print(f"Hexadecimal : {nombre:x}")
print(f"Octal : {nombre:o}")
```

#### Notation scientifique
```python
grand_nombre = 123456789

print(f"{grand_nombre:e}")
print(f"{grand_nombre:.2e}")
```

#### Afficher des accolades
```python
print(f"{{nom}} = {nom}")
print(f"{{age}} = {age}")
```

#### Dates
```python
from datetime import datetime

date = datetime.now()

print(f"Date : {date:%d/%m/%Y}")
print(f"Heure : {date:%H:%M:%S}")
print(f"Date et heure : {date:%d/%m/%Y a %H:%M:%S}")
```

#### Debug rapide avec = 
```python
print(f"{nom=}")
print(f"{age=}")
print(f"{prix=:.2f}")
```
