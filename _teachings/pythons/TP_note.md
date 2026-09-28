---
layout: page
title: Python - TP note
permalink: /enseignement/python/tp_note
toc:
  sidebar: right
---

# Exercice - À vous de jouer

On considère maintenant le système :

$$
\dot{x} = v
$$

$$
\dot{v} = u - 0.5v
$$

La mesure reste :

$$
Y = x
$$

La consigne est :

$$
x_d = 5
$$

Le contrôleur doit utiliser :

$$
u_r = 2 (x_d - x)
$$

Le contrôleur doit utiliser :

$$
u = u_r - k_v v
$$

## Travail demandé

Faire une simulation de $10$ s avec un pas de temps de $0.01$ s pour $k_v = 2$ Hz

Compléter un programme permettant de :

1. créer la fonction `model(X, U)` ;
2. créer la fonction `h(X)` ;
3. créer la fonction `guidance(X, Xd)` ;
4. créer la fonction `ctrl(X, u_r, k_v)` ;
5. créer le vecteur temps ;
6. initialiser le système ;
7. créer les vecteurs de stockage ;
8. réaliser la boucle de simulation ;
9. utiliser Euler pour intégrer le système ;
10. visualiser la position et la consigne ;
11. visualiser la vitesse ;
12. visualiser la commande.

### Structure imposée

La boucle doit respecter :

```python
for t in times:

    # Consigne

    # Guidance

    # Contrôle

    # Modèle

    # Euler

    # Mesure

    # Stockage
```

### Bonus

Comparer les résultats pour :

```
kv_values = [0.5, 1, 2, 5]
```

et visualiser les quatre simulations sur le même graphique.






## Bareme :

- 5 points pour la syntaxe
- 2 points pour l'initialisation des vecteurs et des variables de stockage
- 2 points pour les fonctions guidance et ctrl
- 1 point pour l'intégration d'Euler explicite
- 2 points pour la fonction de mesure
- 2 points pour la fonction model
- 2 points pour le stockage des données
- 1 point pour l'affichage
- 2 points pour la réussite du code
