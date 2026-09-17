import random

produits = ["ordinateur", "souris", "clavier", "casque"]
prix = [800, 30, 50, 70]

panier = []
quantites = []


# Afficher les produits et leurs prix
print("========== produits ==========")

for i in range(len(produits)):
    print(produits[i], ":", prix[i], "euros")


# Fonction pour calculer le total
def calculer_total():
    total = 0

    for i in range(len(panier)):
        produit = panier[i]

        # Chercher le prix du produit
        for j in range(len(produits)):
            if produits[j] == produit:
                total = total + prix[j] * quantites[i]

    return total


# Achats
while True:
    choix = input("\nQuel produit voulez-vous acheter ? (stop pour terminer) : ")

    if choix == "stop":
        break

    if choix in produits:
        quantite = int(input("Quelle quantite voulez-vous ? "))

        panier.append(choix)
        quantites.append(quantite)

        print(choix, "ajoute au panier !")

    else:
        print("Ce produit n'existe pas.")


# Calcul du total
total = calculer_total()


# Reduction aleatoire
reduction = random.randint(0, 20)

montant_reduction = total * reduction / 100
prix_final = total - montant_reduction


# Resume
print("\n========== resume ==========")

print("Produits achetes :", len(panier))
print("Total :", total, "euros")
print("Reduction :", reduction, "%")
print("Prix final :", prix_final, "euros")


# Afficher les produits du panier
print("\n========== panier ==========")

for i in range(len(panier)):
    print(panier[i], "x", quantites[i])


# Chercher le produit le plus cher
if len(panier) > 0:

    produit_plus_cher = panier[0]
    prix_plus_cher = 0

    # Trouver le prix du premier produit
    for i in range(len(produits)):
        if produits[i] == produit_plus_cher:
            prix_plus_cher = prix[i]

    # Comparer avec les autres produits
    for i in range(len(panier)):

        prix_actuel = 0

        for j in range(len(produits)):
            if produits[j] == panier[i]:
                prix_actuel = prix[j]

        if prix_actuel > prix_plus_cher:
            prix_plus_cher = prix_actuel
            produit_plus_cher = panier[i]

    print("\nProduit le plus cher :", produit_plus_cher)
    print("Prix :", prix_plus_cher, "euros")
