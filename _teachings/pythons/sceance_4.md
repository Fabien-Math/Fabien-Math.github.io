---
layout: page
title: Python - Scéance 4
permalink: /enseignement/python/sceance4
toc:
  sidebar: right
---
# Simulation et commande d'un système dynamique

## Objectifs

- définir un système dynamique sous forme d'état ;
- créer une fonction `model(X, U)` ;
- définir une fonction de mesure `h(X)` ;
- intégrer un système dynamique avec Euler ;
- construire une boucle de simulation ;
- définir une fonction de guidage ;
- définir une fonction de commande ;
- stocker les résultats d'une simulation ;
- représenter les résultats ;
- comparer plusieurs simulations.

L'architecture générale d'une simulation est :
```
Consigne -> Guidance -> Contrôleur -> U -> Modèle -> dX -> Euler -> X -> h -> Y -> Sauvegarde
```

## Petit mot...

### Convention de notation : 

les variables représentant des vecteurs ou matrices du modèle (X, U, Y) utilisent des majuscules afin de rester cohérentes avec les notations mathématiques du cours. Les noms des variables scalaires sont écrits en snake_case.

## 1. Le système dynamique

On considère une masse qui se déplace sur une ligne.

```
        x
    ─────────────●──────────────────►
                masse
```

L'état du système est :

$$
X =
\begin{bmatrix}
x \\
v
\end{bmatrix}
$$

avec :

- $x$ : position [m]
- $v$ : vitesse [m/s]

La commande est :

$$
U =
\begin{bmatrix}
u
\end{bmatrix}
$$

où $u$ est l'accélération [m/s²].

Le système dynamique est :

$$
\dot{x} = v
$$

$$
\dot{v} = u
$$

On peut donc écrire :

$$
\dot{X} =
\begin{bmatrix}
\dot{x} \\
\dot{v}
\end{bmatrix}
=
\begin{bmatrix}
v \\
u
\end{bmatrix}
$$


## Dimensions des variables

Dans notre simulation :

$$
X \in \mathbb{R}^{2 \times 1}
$$

$$
U \in \mathbb{R}^{1 \times 1}
$$

$$
\dot{X} \in \mathbb{R}^{2 \times 1}
$$

On aura donc :

```python
X = [[x],
     [v]]

U = [[u]]

dX = [[dx],
      [dv]]
```

Il est important de conserver ces dimensions pendant toute la simulation.


# 2. Le modèle dynamique

Le rôle de la fonction `model` est de calculer la dérivée de l'état.

Elle prend en entrée :

- `X` : état actuel ;
- `U` : commande actuelle.

Elle retourne :

- `dX` : dérivée de l'état.

On veut donc construire :

```text
U -> Modèle -> dX
```

 Pour notre système :

$$
\dot{x} = v
$$

$$
\dot{v} = u
$$


```python
def model(X, U):
    x, v = X.flatten()

    dx = v
    dv = U[0, 0]

    return np.array([[dx], [dv]])
```

## Vérification (N'oubliez pas de tester !)

On peut tester le modèle avec :

$$
x = 2, v = 3, u = 1
$$


On doit obtenir :

$$
\dot{x} = 3, \dot{v} = 1
$$


### Cellule Code
```python
X = np.array([[2], [3]])
U = np.array([[1]])

dX = model(X, U)

print("X =")
print(X)

print("U =")
print(U)

print("dX =")
print(dX)
```


## Exercice 1

Modifier les valeurs de `X` et `U`.

Vérifier que :

$$
\dot{x} = v
$$

et :

$$
\dot{v} = u
$$

Essayez par exemple :

```python
X = np.array([[5], [-2]])
U = np.array([[4]])
```



# 3. La fonction de mesure

Le système possède deux états :

$$
X =
\begin{bmatrix}
x \\
v
\end{bmatrix}
$$

mais supposons que notre capteur mesure uniquement la position.

La sortie est donc :

$$
Y = x
$$

On définit une fonction :

```text
X -> h() -> Y
```

La fonction `h` permet de séparer :

- l'état interne du système ;
- les grandeurs que l'on observe ou mesure.

### Cellule Code

```python
def h(X):
    return np.array([[X[0, 0]]])

X = np.array([[2], [3]])

Y = h(X)

print("X =")
print(X)

print("Y =")
print(Y)
```


Ici :

```python
X = [[x],
     [v]]

Y = [[x]]
```

Donc `X` est de taille `(2, 1)` alors que `Y` est de taille `(1, 1)`.


# 4. Intégration d'Euler explicite


Le modèle donne une dérivée :

$$
\dot{X} = f(X, U)
$$

Mais nous voulons connaître l'état au temps suivant.

La méthode d'Euler explicite donne :

$$
X_{k+1} = X_k + \Delta t \dot{X}_k
$$

En Python :

```python
X = X + dX * dt
```

où :

- `X` est l'état actuel ;
- `dX` est sa dérivée ;
- `dt` est le pas de temps.

### Exemple

Si :

$$
X =
\begin{bmatrix}
2 \\
3
\end{bmatrix}
\quad \text{et} \quad
\dot X =
\begin{bmatrix}
3 \\
1
\end{bmatrix}
$$

avec $dt = 0.1$

alors :

$$
X_{k+1}
=
\begin{bmatrix}
2 \\
3
\end{bmatrix}
+
0.1
\begin{bmatrix}
3 \\
1
\end{bmatrix}
$$

donc :

$$
X_{k+1}
=
\begin{bmatrix}
2.3 \\
3.1
\end{bmatrix}
$$


### Cellule Code

```python
X = np.array([[2], [3]])
dX = np.array([[3], [1]])

dt = 0.1

X = X + dX * dt

print(X)
```


# 5. Première boucle de simulation

Nous allons maintenant simuler le système.

On impose une accélération constante :

$$
u = 1
$$

Le système part de :

$$
x(0) = 0
$$

$$
v(0) = 0
$$

On définit :

- la durée de simulation ;
- le pas de temps ;
- l'état initial ;
- la commande.


```python
tf = 5
dt = 0.01
times = np.arange(0, tf, dt)

X = np.array([[0], [0]])
U = np.array([[1]])
```


## Boucle de simulation

À chaque instant :

1. on calcule `dX` avec le modèle ;
2. on met à jour `X` avec la méthode d'Euler explicite.

### Cellule Code
```python
for t in times:
    dX = model(X, U)
    X = X + dX * dt

print(X)
```

# 6. Stockage des résultats

À la fin de la simulation, nous ne possédons que l'état final.

Pour tracer l'évolution du système, il faut conserver les états à chaque instant.

On crée :

```python
X_vec = np.zeros((2, 0))
```

On ajoute ensuite chaque nouvel état comme une colonne :

```python
X_vec = np.hstack((X_vec, X))
```

On obtient :

```
          t0    t1    t2    t3    ...

x         x0    x1    x2    x3
v         v0    v1    v2    v3
```


### Cellule Code

```python
tf = 5
dt = 0.01
times = np.arange(0, tf, dt)

X = np.array([[0], [0]])
U = np.array([[1]])

X_vec = np.zeros((2, 0))

for t in times:
    dX = model(X, U)
    X = X + dX * dt

    X_vec = np.hstack((X_vec, X))

plt.figure()

plt.plot(times, X_vec[0, :], label='Position')
plt.plot(times, X_vec[1, :], label='Vitesse')

plt.xlabel('Temps (s)')
plt.grid()
plt.legend()
plt.show()
```

# 7. Ajouter la mesure

Nous allons maintenant utiliser `h(X)` dans la boucle.

La chaîne devient :

```text
X -> Modèle -> dX -> Euler -> X -> h -> Y
```

Nous allons également stocker `Y`.


### Cellule Code

```python
Y_vec = np.zeros((1, 0))

X = np.array([[0], [0]])

for t in times:
    dX = model(X, U)
    X = X + dX * dt

    Y = h(X)

    X_vec = np.hstack((X_vec, X))
    Y_vec = np.hstack((Y_vec, Y))
```

# 8. Ajouter une commande

Jusqu'ici, l'accélération était imposée :

$$
u = 1
$$

Nous voulons maintenant que le système atteigne une position souhaitée :

$$
x_d = 5
$$

Nous avons besoin d'un contrôleur.

On choisit un contrôleur de type Proportionnel-Dérivé :

$$
u = K_p(x_d-x)-K_dv
$$

où :

- $K_p$ contrôle l'erreur de position ;
- $K_d$ agit sur la vitesse ;
- $x_d-x$ est l'erreur de position.

L'objectif est :

$$
x \rightarrow x_d
$$


# 9. Fonction de guidance

Dans une architecture de commande, on peut séparer :

```text
Consigne
   ↓
Guidance
   ↓
Référence
   ↓
Contrôleur
   ↓
Commande
```

La fonction `guidance` calcule ici l'accélération de référence.

Elle reçoit :

- l'état `X` ;
- la consigne `Xd`.

Elle retourne :

- `ud`.


### Cellule Code

```python
kp = 2
kd = 1

def guidance(X, Xd, kp, kd):
    x, v = X.flatten()

    ud = kp * (Xd - x) - kd * v

    return ud
```

Dans cette fonction :

$$
e = x_d-x
$$

puis :

$$
u_d = K_p e-K_dv
$$

Le terme $K_p e$ pousse le système vers la consigne.

Le terme $-K_dv$ permet de tenir compte de la vitesse du système.

# 10. Fonction de contrôle

La fonction `ctrl` transforme la référence de commande `ud` en commande du système `U`.

Ici, le contrôleur est volontairement très simple :

$$
U =
\begin{bmatrix}
u_d
\end{bmatrix}
$$

### Cellule Code

```python
def ctrl(X, ud):
    return np.array([[ud]])
```


# 11. Boucle de simulation avec commande

Nous avons maintenant toutes les fonctions nécessaires.

À chaque instant :

1. définir la consigne ;
2. calculer la référence avec `guidance` ;
3. calculer la commande avec `ctrl` ;
4. calculer la dynamique avec `model` ;
5. intégrer avec Euler ;
6. mesurer avec `h` ;
7. stocker les résultats.

La boucle est donc :

```text
Xd -> Guidance -> ud -> Contrôleur -> U -> Modèle -> dX -> Euler -> X -> h -> Y
```


### Cellule Code

```python
tf = 10
dt = 0.05
times = np.arange(0, tf, dt)

X = np.array([[0], [0]])
dX = np.array([[0], [0]])
Y = np.array([[0]])
U = np.array([[0]])

X_vec = np.zeros((2, 0))
Y_vec = np.zeros((1, 0))
U_vec = np.zeros((1, 0))
Y_d_vec = np.zeros((1, 0))

for t in times:
    Xd = 5
    Y_d = np.array([[Xd]])

    ud = guidance(X, Xd, kp, kd)
    U = ctrl(X, ud)

    dX = model(X, U)
    X = X + dX * dt

    Y = h(X)

    X_vec = np.hstack((X_vec, X))
    Y_vec = np.hstack((Y_vec, Y))
    U_vec = np.hstack((U_vec, U))
    Y_d_vec = np.hstack((Y_d_vec, Y_d))
```

# 12. Visualisation des résultats

Nous pouvons maintenant afficher :

- la position ;
- la consigne ;
- la vitesse ;
- la commande.


### Cellule Code

```python
plt.figure(figsize=(8, 4))

plt.plot(times, Y_vec[0, :], label='Position')
plt.plot(times, Y_d_vec[0, :], '--', label='Consigne')

plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(8, 4))

plt.plot(times, X_vec[1, :], label='Vitesse')

plt.xlabel('Temps (s)')
plt.ylabel('Vitesse (m/s)')
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(8, 4))

plt.plot(times, U_vec[0, :], label='Commande', color='green')

plt.xlabel('Temps (s)')
plt.ylabel('Accélération (m/s²)')
plt.grid()
plt.legend()
plt.show()
```

# 13. Comparer plusieurs contrôleurs

Nous allons maintenant faire plusieurs simulations.

On souhaite comparer différentes valeurs de $K_p$ :

$$
K_p \in \{0.5,\ 1,\ 2,\ 5\}
$$

Chaque simulation doit :

1. repartir du même état initial ;
2. utiliser une valeur différente de `kp` ;
3. être simulée sur toute la durée ;
4. stocker son résultat ;
5. être affichée avec les autres.

### Cellule Code

```python
kp_values = [0.5, 1, 2, 5]

results = np.zeros((len(kp_values), len(times)))

for j, kp in enumerate(kp_values):
    X = np.array([[0], [0]])

    for i, t in enumerate(times):
        Xd = 5

        ud = guidance(X, Xd, kp, kd)
        U = ctrl(X, ud)

        dX = model(X, U)
        X = X + dX * dt

        results[j, i] = X[0, 0]

plt.figure(figsize=(8, 5))

for j, kp in enumerate(kp_values):
    plt.plot(times, results[j, :], label=f'kp = {kp}')

plt.axhline(5, color='black', linestyle='--', label='Consigne')

plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.legend()
plt.show()
```
