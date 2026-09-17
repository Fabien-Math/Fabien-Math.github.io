---
layout: page
title: Python - Imports
permalink: /enseignement/python_scripts/cours_imports
toc:
  sidebar: right
---

[Fichier brut](cours_imports.py)


#### Importer un module entier
```python
import math

print("Racine carree de 25 :", math.sqrt(25))
```

#### Importer une fonction precise
```python
from math import sqrt

print("Racine carree de 36 :", sqrt(36))
```

#### Donner un autre nom a un module
```python
import random as hasard

nombre = hasard.randint(1, 10)
print("Nombre aleatoire :", nombre)
```

#### Importer plusieurs elements d'un module
```python
from math import pi, floor

print("Valeur de pi :", pi)
print("floor(4.8) :", floor(4.8))
```

#### Importer son propre module
```python
from utils.module import dire_bonjour
import utils.module as module

dire_bonjour()
module.dire_bonjour()
```



### Questions

#### Ou dans le programme vont les imports ?

#### Correct ou incorrect ?
```python
from math import *
import numpy as plt
from scipy.spatial.transform import Rotation as R
```