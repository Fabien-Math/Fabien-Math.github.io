"""
Il manque quelques mots dans les 'print' pour plus de clarte.
Ne mettez pas d'accent, restez sur des caracteres ASCII.

Nom de variable plus precise --> position ou pos_robot en fr ou robot_pos est preferable ici

Pas d'espace entre les fonctions et (), pareil pour les listes et tous les objets 'callable' --> 
Correct : print(), liste[]
Incorrect : print (), liste []

Espace avant et apres les operateurs -->
Correct : a + b, a > b, l[0] += 1
Incorrect :  a +b, a>b, l[0]+=1

Pas d'espace avant ':' -->
Correct : for i in range(5):
Incorrect : while True :
"""


# Correction :
from utils import visualize_traj

# Initialisation du robot
x = 0
y = 0

position = (x, y)
trajectory = [position]
print(f"Position du robot : {position}")


# Deplacement du robot
dx = 1
dy = 0

x += dx
y += dy

position = (x, y)
trajectory.append(position)

print(f"Position du robot : {position}")

# Sequence de mouvements cartesiens
moves = [
    (1, 0),
    (0, 1),
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

for dx, dy in moves:
    x += dx
    y += dy

    position = (x, y)
    trajectory.append(position)

    print(f"Position du robot : {position}")


visualize_traj(trajectory)