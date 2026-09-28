"""
Il manque quelques mots dans les 'print' pour plus de clarte.
Ne mettez pas d'accent, restez sur des caracteres ASCII.

Nom de variable plus precise --> pos_robot en fr ou robot_pos est preferable ici

Pas d'espace entre les fonctions et (), pareil pour les listes et tous les objets 'callable' --> 
Correct : print(), liste[]
Incorrect : print (), liste []

Espace avant et apres les operateurs -->
Correct : a + b, a > b, l[0] += 1
Incorrect :  a +b, a>b, l[0]+=1

Pas d'espace avant ':' -->
Correct : for i in range(5):
Incorrect : while True :

Faites votre code de facon a ce que quelqu'un d'exterieur puisse le comprendre (a la lecture et a l'execution)
Mettez vos binomes en copie !
"""



# Correction :

# Visualisation dans le terminal
def visualize_traj(trajectory):
    xs , ys = zip(*trajectory)
    x_min, x_max = min(xs) - 1, max(xs) + 1
    y_min, y_max = min(ys) - 1, max(ys) + 1

    # Top line
    print("_" * int(3.5*(x_max - x_min)))
    for y in range(y_max, y_min - 1, -1):
        row = ""
        for x in range(x_min, x_max + 1):
            if (x, y) in trajectory:
                step = trajectory.index((x, y))
                row += f"{step:2} "
            else:
                row += " . "
        print(row)
    # Bottom line
    print("_" * int(3.5*(x_max - x_min)))

# Visualisation dans le terminal
def visualize_traj_opti(trajectory):
    xs , ys = zip(*trajectory)
    x_min, x_max = min(xs) - 1, max(xs) + 1
    y_min, y_max = min(ys) - 1, max(ys) + 1

    grid = [[' . ' for _ in range(x_max - x_min + 1)] for _ in range(y_max - y_min + 1)]
    for i, (x, y) in enumerate(trajectory):
        grid[(y_max - y_min) - (y - y_min)][x - x_min] = f" {i} "

    # Top line
    print("_" * int(3.5*(x_max - x_min)))
    for row in grid:
        print(''.join(row))
    # Bottom line
    print("_" * int(3.5*(x_max - x_min)))


# Initialisation du robot
x = 0
y = 0

position = (x, y)
traj = [position]
print(f"Position du robot : {position}")


# Deplacement du robot
dx = 1
dy = 0

x += dx
y += dy

position = (x, y)
traj.append(position)

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
    traj.append(position)

    print(f"Position du robot : {position}")

visualize_traj(traj)
visualize_traj_opti(traj)
