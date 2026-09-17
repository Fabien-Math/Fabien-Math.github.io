# Les imports en python


# Importer un module entier
import math

print("Racine carree de 25 :", math.sqrt(25))
input()







# Importer une fonction precise
from math import sqrt

print("Racine carree de 36 :", sqrt(36))
input()







# Donner un autre nom a un module
import random as hasard

nombre = hasard.randint(1, 10)
print("Nombre aleatoire :", nombre)
input()







# Importer plusieurs elements d'un module
from math import pi, floor

print("Valeur de pi :", pi)
print("floor(4.8) :", floor(4.8))
input()







# Importer son propre module
from utils.module import dire_bonjour
import utils.module as module

dire_bonjour()
module.dire_bonjour()

exit()





### Questions

# Ou dans le programme vont les imports ?

# Correct ou incorrect ?
from math import *
import numpy as plt
from scipy.spatial.transform import Rotation as R
