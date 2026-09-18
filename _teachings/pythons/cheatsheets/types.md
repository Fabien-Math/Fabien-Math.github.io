---
layout: page
title: Python — Data types
permalink: /enseignement/cheatsheets/python/data_types
toc:
  sidebar: right
---

| Catégorie  | Type         | Exemple                 | Description                                    |
| ---------- | ------------ | ----------------------- | ---------------------------------------------- |
| Numérique  | `int`        | `42`                    | Nombre entier                                  |
| Numérique  | `float`      | `3.14`                  | Nombre à virgule flottante                     |
| Numérique  | `complex`    | `2 + 3j`                | Nombre complexe                                |
| Booléen    | `bool`       | `True`                  | Vrai ou faux                                   |
| Texte      | `str`        | `"Python"`              | Chaîne de caractères                           |
| Binaire    | `bytes`      | `b"hello"`              | Séquence d'octets immuable                     |
| Binaire    | `bytearray`  | `bytearray(b"hello")`   | Séquence d'octets modifiable                   |
| Binaire    | `memoryview` | `memoryview(b"hello")`  | Vue sur des données binaires                   |
| Séquence   | `list`       | `[1, 2, 3]`             | Séquence ordonnée et modifiable                |
| Séquence   | `tuple`      | `(1, 2, 3)`             | Séquence ordonnée et immuable                  |
| Séquence   | `range`      | `range(10)`             | Séquence d'entiers                             |
| Ensemble   | `set`        | `{1, 2, 3}`             | Ensemble non ordonné d'éléments uniques        |
| Ensemble   | `frozenset`  | `frozenset({1, 2, 3})`  | Ensemble immuable                              |
| Mapping    | `dict`       | `{"x": 1, "y": 2}`      | Association clé → valeur                       |
| Null       | `NoneType`   | `None`                  | Absence de valeur                              |
| Callable   | `function`   | `def f(): ...`          | Fonction Python                                |
| Callable   | `lambda`     | `lambda x: x + 1`       | Fonction anonyme                               |
| Objet      | `object`     | `object()`              | Classe de base de tous les objets              |
| Classe     | `type`       | `type(int)`             | Type d'un objet / métaclasse                   |
| Exception  | `Exception`  | `ValueError(...)`       | Objet représentant une erreur                  |
| Itérateur  | `iterator`   | `iter([1, 2, 3])`       | Objet permettant d'itérer                      |
| Générateur | `generator`  | `(x for x in range(3))` | Itérateur produisant des valeurs à la demande  |
| Coroutine  | `coroutine`  | `async def f(): ...`    | Objet utilisé avec la programmation asynchrone |
