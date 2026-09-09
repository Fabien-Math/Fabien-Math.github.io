## Exercice 1

### Départ

```python
produits = ["ordinateur", "souris", "clavier", "casque"]
prix = [800, 30, 50, 70]

panier = []
```

### Consignes

1. Afficher les produits et leurs prix avec une boucle `for`.
2. Demander à l'utilisateur quel produit il veut acheter avec `input()`.
3. Vérifier avec `if` si le produit existe dans la liste.
4. Ajouter le produit choisi dans `panier`.
5. Utiliser une boucle `while` pour permettre plusieurs achats.
6. Si l'utilisateur écrit `stop`, terminer les achats.
7. Créer une fonction `calculer_total()` pour calculer le total du panier.
8.  À la fin, afficher :

```
========== resume ==========

produits achetes : 3
total : 880 euros
```

### Bonus

1. Utiliser `random.randint(0, 20)` pour créer une réduction aléatoire entre 0 % et 20 %.
2. Afficher le prix final après réduction.
3. Afficher tous les produits du panier.
4. Afficher le produit le plus cher du panier.
5. Demander la quantité lorsqu'un produit est ajouté au panier.