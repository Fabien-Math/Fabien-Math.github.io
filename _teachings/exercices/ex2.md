---
layout: page
title: Python - Exercice - Gestion d’un inventaire
permalink: /enseignement/python/ex2
toc:
  sidebar: right
---


## Création du dictionnaire

Créer un dictionnaire `inventaire` contenant les produits suivants :

- `"ordinateur"` : 5
- `"souris"` : 12
- `"clavier"` : 8
- `"casque"` : 3

Afficher le dictionnaire.

## Accéder aux données

Afficher :

- le nombre d’ordinateurs disponibles ;
- le nombre de casques disponibles ;
- uniquement les noms des produits.

## Modifier le stock

Le magasin reçoit :

- 3 ordinateurs supplémentaires ;
- 5 casques supplémentaires.

Modifier le dictionnaire en conséquence, puis afficher le nouveau stock.

## Ajouter un produit

Ajouter un nouveau produit avec la quantité associée :

```
"webcam": 6
```

Afficher le dictionnaire.

## Supprimer un produit

Le magasin ne vend plus de souris.

Supprimer `"souris"` du dictionnaire.

Afficher ensuite le dictionnaire.

## Parcourir le dictionnaire

Utiliser une boucle `for` pour afficher chaque produit sous la forme suivante :

```
ordinateur : 8
clavier : 8
casque : 8
webcam : 6
```

## Rechercher un produit

Demander à l’utilisateur d’entrer le nom d’un produit.

Si le produit existe dans le dictionnaire, afficher son stock.

Sinon, afficher :

```
Produit inconnu
```

## Calculer le stock total

Calculer le nombre total d’objets disponibles dans le magasin.

Afficher le résultat sous la forme :

```
Stock total : 30
```

Utiliser une boucle `for` pour parcourir les quantités du dictionnaire.

## Bonus - Valeur de l’inventaire

Créer un dictionnaire contenant le prix de chaque produit :

```
prix = {
"ordinateur": 800,
"clavier": 50,
"casque": 80,
"webcam": 60
}
```

Pour chaque produit, calculer la valeur de son stock.

Par exemple :

```
ordinateur : 8 x 800 = 6400 €
```

Puis calculer et afficher la valeur totale de l’inventaire.

```
Valeur totale du stock : XXXX €
```