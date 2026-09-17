---
layout: page
title: Python - Types basiques
permalink: /enseignement/python_scripts/demo_matplotlib
toc:
  sidebar: left
---


```python
import numpy as np
import matplotlib.pyplot as plt
import utils.plotting_params

# Donnees du robot
time = np.linspace(0, 20, 500)
dt = time[1] - time[0]

x = 5 * np.cos(time / 8) + time * 0.4
y = 5 * np.sin(time / 8) + time * 0.15

v_x = 0.8 + 0.3 * np.sin(time / 4)
v_y = 0.2 + 0.5 * np.sin(time / 2.5) * np.cos(time)
v = np.sqrt(v_x**2 + v_y**2)

a_x = np.gradient(v_x, time)
a_y = np.gradient(v_y, time)
a = np.sqrt(a_x**2 + a_y**2)

x = np.cumsum(v_x * dt)
y = np.cumsum(v_y * dt)

battery = 100 - 0.03 * (np.cumsum(a)) * time

temperature = 38 + 7 * a + np.random.normal(0, 0.5, len(time))

sensor_error = (0.05 * np.sin(time) + np.random.normal(0, 0.02, len(time)))

plt.plot(time, v_x)
plt.show()
```


## Simple plot
```python
# 1. Trajectoire du robot
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(
    x,
    y,
    color="blue",
    linewidth=2,
    label="Trajectoire"
)

ax.scatter(
    x[0],
    y[0],
    color="green",
    s=150,
    label="Depart",
    zorder=5
)

ax.scatter(
    x[-1],
    y[-1],
    color="red",
    s=150,
    label="Arrivee",
    zorder=5
)

ax.set_title("Trajectoire du robot")
ax.set_xlabel("Position X (m)")
ax.set_ylabel("Position Y (m)")

ax.axis("equal")
ax.grid(True)
ax.legend()

plt.show()
```


## Plot multiple avec axes partagés
```python
# 2. Vitesse du robot
fig, axs = plt.subplots(2, sharex=True, sharey=True, figsize=(12, 4*2))


for ax, v_i, axis in zip(axs, (v_x, v_y), "XY"):
    ax.plot(
        time,
        v_i,
        color="orange",
    )

    ax.axhline(
        0,
        color="black",
        linestyle="--"
    )


    ax.set_title(f"Vitesse du robot selon {axis}")
    ax.set_xlabel("Temps (s)")
    ax.set_ylabel("v (m/s)")

    ax.grid(True)

plt.show()
```## Plot multiple avec un axe partagé
```python
# 3. Acceleration
fig, axs = plt.subplots(2, sharex=True, figsize=(12, 4*2))

for ax, a_i, axis in zip(axs, (a_x, a_y), "XY"):
    ax.plot(
        time,
        a_i,
        color="purple",
    )

    ax.axhline(
        0,
        color="black",
        linestyle="--"
    )

    ax.set_title(f"Acceleration du robot selon {axis}")
    ax.set_xlabel("Temps (s)")
    ax.set_ylabel("a (m/s²)")

    ax.grid(True)

plt.show()
```


## Plot avec fill_between

```python
# 4. Batterie
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    time,
    battery,
    color="green",
    linewidth=3
)

ax.fill_between(
    time,
    battery,
    alpha=0.2,
    color="green"
)

ax.axhline(
    20,
    color="red",
    linestyle="--",
    label="Seuil critique"
)

ax.set_title("Niveau de batterie")
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Batterie (%)")

ax.set_ylim(0, 105)

ax.grid(True)
ax.legend()

plt.show()
```

## Plot avec axhline

```python
# 5. Temperature des moteurs
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    time,
    temperature,
    color="red",
    label="Temperature moteur"
)

ax.axhline(
    40,
    color="orange",
    linestyle="--",
    label="Seuil attention"
)

ax.axhline(
    45,
    color="darkred",
    linestyle="--",
    label="Seuil critique"
)

ax.set_title("Temperature des moteurs")
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Temperature (°C)")

ax.grid(True)
ax.legend()

plt.show()
```


## Plot avec axhline et fill_between

```python
# 6. Erreur des capteurs
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    time,
    sensor_error,
    color="red",
    linewidth=1,
    label="Erreur capteur"
)

ax.axhline(
    0,
    color="black",
    linestyle="--"
)

ax.fill_between(
    time,
    sensor_error,
    0,
    alpha=0.2,
    color="red"
)

ax.set_title("Erreur du capteur de position")
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Erreur (m)")

ax.grid(True)
ax.legend()

plt.show()

```


## Plot multiple

```python
# 7. Comparaison trajectoire reelle / trajectoire ideale
ideal_x = time * 0.8
ideal_y = time * 0.3

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(
    ideal_x,
    ideal_y,
    color="black",
    linestyle="--",
    linewidth=2,
    label="Trajectoire ideale"
)

ax.plot(
    x,
    y,
    color="blue",
    linewidth=2,
    label="Trajectoire reelle"
)

ax.set_title("Comparaison des trajectoires")
ax.set_xlabel("Position X (m)")
ax.set_ylabel("Position Y (m)")

ax.axis("equal")
ax.grid(True)
ax.legend()

plt.show()
```


## Plot avec scatter

```python
# 8. Carte des obstacles
obstacle_x = [3, 4, 5, 8, 9, 12, 13, 14, 17, 18]
obstacle_y = [2, 2.5, 2, 5, 6, 3, 4, 3.5, 7, 6.5]

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(
    x,
    y,
    color="blue",
    linewidth=2,
    label="Robot"
)

ax.scatter(
    obstacle_x,
    obstacle_y,
    color="black",
    marker="s",
    s=100,
    label="Obstacle"
)

ax.scatter(
    x[0],
    y[0],
    color="green",
    s=150,
    label="Depart"
)

ax.scatter(
    x[-1],
    y[-1],
    color="red",
    s=150,
    label="Arrivee"
)

ax.set_title("Carte de navigation")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")

ax.axis("equal")
ax.grid(True)
ax.legend()

plt.show()
```


## Plot avec imshow

```python
# 9. Carte de chaleur des capteurs
sensor_x = np.linspace(-10, 10, 50)
sensor_y = np.linspace(-10, 10, 50)

X, Y = np.meshgrid(
    sensor_x,
    sensor_y
)

distance = np.sqrt(X**2 + Y**2)

sensor_data = np.exp(-distance / 10)

fig, ax = plt.subplots(figsize=(9, 7))

heatmap = ax.imshow(
    sensor_data,
    extent=[
        sensor_x.min(),
        sensor_x.max(),
        sensor_y.min(),
        sensor_y.max()
    ],
    origin="lower",
    cmap="viridis"
)

fig.colorbar(
    heatmap,
    ax=ax,
    label="Intensite du signal"
)

ax.set_title("Carte de chaleur du capteur")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")

plt.show()
```


## Plot multiple - tableau

```python
# 10. Tableau de bord robotique
fig, axes = plt.subplots(
    2,
    2,
    figsize=(14, 9)
)


# Trajectoire
axes[0, 0].plot(
    x,
    y,
    color="blue"
)

axes[0, 0].set_title("Trajectoire")
axes[0, 0].set_xlabel("X (m)")
axes[0, 0].set_ylabel("Y (m)")
axes[0, 0].axis("equal")
axes[0, 0].grid(True)


# Vitesse
axes[0, 1].plot(
    time,
    v,
    color="orange"
)

axes[0, 1].set_title("Norme de la vitesse")
axes[0, 1].set_xlabel("Temps (s)")
axes[0, 1].set_ylabel("m/s")
axes[0, 1].grid(True)


# Batterie
axes[1, 0].plot(
    time,
    battery,
    color="green"
)

axes[1, 0].axhline(
    20,
    color="red",
    linestyle="--"
)

axes[1, 0].set_title("Batterie")
axes[1, 0].set_xlabel("Temps (s)")
axes[1, 0].set_ylabel("%")
axes[1, 0].grid(True)

# Temperature
axes[1, 1].plot(
    time,
    temperature,
    color="red"
)

axes[1, 1].axhline(
    40,
    color="orange",
    linestyle="--"
)

axes[1, 1].set_title("Temperature")
axes[1, 1].set_xlabel("Temps (s)")
axes[1, 1].set_ylabel("°C")
axes[1, 1].grid(True)


fig.suptitle(
    "Tableau de bord du robot",
    fontsize=18,
    fontweight="bold"
)

plt.show()
```