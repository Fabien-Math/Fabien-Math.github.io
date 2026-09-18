---
layout: page
title: Python - TP
permalink: /enseignement/python/TP1
toc:
  sidebar: right
---

[Commentaires et correction](/assets/codes/python/exercices/commantaires_general.py)

## Objectif

Programmer un robot virtuel capable de se déplacer dans le plan et visualiser ses trajectoires.

## Niveaux

### Niveau 1

Initialisation du robot et affichages.

### Niveau 2

Faire bouger le robot et affichages.

### Niveau 3

Faire bouger le robot avec une séquence de mouvements cartésiens fixe de 1m et affichages.

### Niveau 4

Aller vers des points donnés ((0,4), (2,1), (2,3), (4,0)) en utilisant des directions cartésiennes et des déplacements de 1m.

### Niveau 5

Mémoriser la trajectoire.

### Niveau 6

Visualiser la trajectoire dans le terminal en affichant une grille vide avec des croix aux positions traversées par le robot.

*On pourra remplacer les croix par des numéros pour visualiser la temporalité.*

### Niveau 7

Se déplacer librement dans le plan toujours avec un pas de 1m maximum et affichage.

### Niveau 8

Créer une fonction de déplacement avec un pas de déplacement en paramètre.

### Niveau 9

Ajouter une vitesse au robot et le faire se déplacer avec un pas de temps $\Delta t$ et affichage.

### Niveau 10

Déplacements autonomes de point en point en faisant varier la vitesse.

- Vitesse maximale autorisée selon x : 1 m/s
- Vitesse maximale autorisée selon y : 0.5 m/s

### Niveau 11

Visualisation simple avec Matplotlib.

### Niveau 12

Visualisation en temps réel simple avec Matplotlib.

### Niveau 13

Passage à NumPy.

### Niveau 14

Simulation de plusieurs robot et affichage comparatif. Chaque robot a sa mission.

### Niveau 15

Ajouter des obstacles à l'environnement.

### Niveau 16

Créer une fonction permettant de calculer la distance entre le robot et un obstacle.

### Niveau 17

Détecter les collisions avec les obstacles.
Si une collision est détectée, générer un mouvement aléatoire (ou non) pour débloquer le robot

### Niveau 18

Déplacements autonomes de point en point avec des obstacles sans plannification (le robot ne connaît pas la carte du monde).

### Niveau 19

Définir une distance minimale de sécurité autour du robot (détection dans un rayon de 50 cm).

### Niveau 20

Ajouter un modèle au robot

Le robot possède deux roues motrices placées sur un même axe, symétriquement par rapport au centre du robot.
Chaque roue est située à `r = 0.20` m du centre. L'entraxe entre les deux roues est donc de `d = 40` cm

### Niveau 21

Créer un système simple d'évitement d'obstacle.

Lorsque le robot détecte un obstacle :
- contourner l'obstacle;
- reprendre la direction de l'objectif.

Le système n'a pas besoin de trouver la trajectoire optimale.

### Niveau 22

Comparer plusieurs trajectoires possibles.

Pour chaque trajectoire, calculer :
- sa longueur 
- le nombre de changements de direction 
- le temps nécessaire.

Afficher les résultats afin de comparer les trajectoires.