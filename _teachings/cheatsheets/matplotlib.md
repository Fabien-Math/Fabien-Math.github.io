---
layout: page
title: Python — MatPlotLib
permalink: /enseignement/cheatsheets/matplotlib
toc:
  sidebar: right
---


| Catégorie           | Fonction / objet     | Exemple                                  | Description                                |
| ------------------- | -------------------- | ---------------------------------------- | ------------------------------------------ |
| Import              | `plt`                | `import matplotlib.pyplot as plt`        | Convention courante pour importer Pyplot   |
| Figure              | `plt.figure()`       | `plt.figure(figsize=(8, 5))`             | Crée une nouvelle figure                   |
| Affichage           | `plt.show()`         | `plt.show()`                             | Affiche le graphique                       |
| Courbe              | `plt.plot()`         | `plt.plot(x, y)`                         | Crée une courbe                            |
| Points              | `plt.scatter()`      | `plt.scatter(x, y)`                      | Crée un nuage de points                    |
| Barres              | `plt.bar()`          | `plt.bar(x, values)`                     | Crée un graphique en barres                |
| Barres horizontales | `plt.barh()`         | `plt.barh(x, values)`                    | Crée des barres horizontales               |
| Histogramme         | `plt.hist()`         | `plt.hist(data, bins=10)`                | Crée un histogramme                        |
| Camembert           | `plt.pie()`          | `plt.pie(values)`                        | Crée un graphique circulaire               |
| Boxplot             | `plt.boxplot()`      | `plt.boxplot(data)`                      | Affiche la distribution des données        |
| Courbe en escalier  | `plt.step()`         | `plt.step(x, y)`                         | Crée une courbe en escalier                |
| Aire                | `plt.fill_between()` | `plt.fill_between(x, y)`                 | Remplit une zone sous une courbe           |
| Ligne horizontale   | `plt.axhline()`      | `plt.axhline(y=10)`                      | Ajoute une ligne horizontale               |
| Ligne verticale     | `plt.axvline()`      | `plt.axvline(x=5)`                       | Ajoute une ligne verticale                 |
| Limites             | `plt.xlim()`         | `plt.xlim(0, 10)`                        | Définit les limites de l'axe X             |
| Limites             | `plt.ylim()`         | `plt.ylim(0, 100)`                       | Définit les limites de l'axe Y             |
| Titre               | `plt.title()`        | `plt.title("Evolution")`                 | Ajoute un titre                            |
| Axe X               | `plt.xlabel()`       | `plt.xlabel("Temps")`                    | Ajoute un nom à l'axe X                    |
| Axe Y               | `plt.ylabel()`       | `plt.ylabel("Valeur")`                   | Ajoute un nom à l'axe Y                    |
| Légende             | `plt.legend()`       | `plt.legend()`                           | Affiche la légende                         |
| Grille              | `plt.grid()`         | `plt.grid(True)`                         | Affiche une grille                         |
| Couleur             | `color`              | `plt.plot(x, y, color="red")`            | Définit la couleur                         |
| Style               | `linestyle`          | `plt.plot(x, y, linestyle="--")`         | Définit le style de ligne                  |
| Épaisseur           | `linewidth`          | `plt.plot(x, y, linewidth=2)`            | Définit l'épaisseur de la ligne            |
| Marqueur            | `marker`             | `plt.plot(x, y, marker="o")`             | Ajoute un marqueur aux points              |
| Transparence        | `alpha`              | `plt.plot(x, y, alpha=0.5)`              | Définit la transparence                    |
| Taille              | `markersize`         | `plt.plot(x, y, markersize=8)`           | Définit la taille des marqueurs            |
| Texte               | `plt.text()`         | `plt.text(2, 5, "Point")`                | Ajoute du texte à une position             |
| Annotation          | `plt.annotate()`     | `plt.annotate("Max", xy=(2, 5))`         | Ajoute une annotation                      |
| Sauvegarde          | `plt.savefig()`      | `plt.savefig("graph.png")`               | Sauvegarde le graphique                    |
| Sous-graphiques     | `plt.subplot()`      | `plt.subplot(2, 1, 1)`                   | Sélectionne un emplacement dans une grille |
| Sous-graphiques     | `plt.subplots()`     | `fig, ax = plt.subplots()`               | Crée une figure et des axes                |
| Axe                 | `ax.plot()`          | `ax.plot(x, y)`                          | Trace sur un objet `Axes`                  |
| Axe                 | `ax.scatter()`       | `ax.scatter(x, y)`                       | Nuage de points sur un objet `Axes`        |
| Axe                 | `ax.set_title()`     | `ax.set_title("Evolution")`              | Définit le titre d'un axe                  |
| Axe                 | `ax.set_xlabel()`    | `ax.set_xlabel("Temps")`                 | Définit le nom de l'axe X                  |
| Axe                 | `ax.set_ylabel()`    | `ax.set_ylabel("Valeur")`                | Définit le nom de l'axe Y                  |
| Axe                 | `ax.legend()`        | `ax.legend()`                            | Affiche la légende                         |
| Axe                 | `ax.grid()`          | `ax.grid(True)`                          | Affiche une grille                         |
| Style global        | `plt.style.use()`    | `plt.style.use("ggplot")`                | Applique un style prédéfini                |
| Colormap            | `cmap`               | `plt.scatter(x, y, c=z, cmap="viridis")` | Définit une palette de couleurs            |
| Couleur par valeur  | `c`                  | `plt.scatter(x, y, c=values)`            | Associe une couleur à chaque valeur        |
| Axe logarithmique   | `plt.xscale()`       | `plt.xscale("log")`                      | Utilise une échelle logarithmique sur X    |
| Axe logarithmique   | `plt.yscale()`       | `plt.yscale("log")`                      | Utilise une échelle logarithmique sur Y    |
| Espacement          | `plt.tight_layout()` | `plt.tight_layout()`                     | Ajuste automatiquement les espacements     |
| Fermeture           | `plt.close()`        | `plt.close()`                            | Ferme une figure                           |

## Types de graphiques à connaître

| Graphique       | Fonction             | Utilisation                       |
| --------------- | -------------------- | --------------------------------- |
| Courbe          | `plt.plot()`         | Évolution d'une donnée            |
| Nuage de points | `plt.scatter()`      | Relation entre deux variables     |
| Barres          | `plt.bar()`          | Comparaison entre catégories      |
| Histogramme     | `plt.hist()`         | Distribution d'une variable       |
| Camembert       | `plt.pie()`          | Répartition entre catégories      |
| Boxplot         | `plt.boxplot()`      | Distribution et valeurs atypiques |
| Aire            | `plt.fill_between()` | Zone sous une courbe              |


## Version recommandée avec `Figure` et `Axes`

Pour des graphiques plus complexes, on utilise généralement l'interface orientée objet :

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 8, 10]

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, y, color="blue", marker="o", label="Donnees")

ax.set_title("Evolution des donnees")
ax.set_xlabel("Temps")
ax.set_ylabel("Valeur")

ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()
```
