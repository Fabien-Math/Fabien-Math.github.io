# Demonstration des f-strings en Python

nom = "Alice"
age = 25
prix = 1234.5678
pourcentage = 0.8567
nombre = 42

print("Inserer une variable")
print(f"Bonjour {nom} !")
print(f"Tu as {age} ans.")
input()














print("\nCalcul dans une f-string")
print(f"Dans 5 ans, tu auras {age + 5} ans.")
print(f"2 x 3 = {2 * 3}")
input()














print("\nNombres decimaux")
print(f"Prix : {prix:.2f}")          # 2 decimales
print(f"Prix : {prix:.1f}")          # 1 decimale
print(f"Prix : {prix:.0f}")          # Arrondi a l'entier
input()














print("\nPourcentages")
print(f"Progression : {pourcentage:.1%}")  # 85.7%
input()














print("\nSeparateur de milliers")
print(f"Nombre : {1234567:,}")        # 1,234,567
print(f"Nombre : {1234567:_}")        # 1_234_567
input()














print("\nLargeur et alignement")
texte = "Python"

print(f"|{texte:<10}|")              # Aligne a gauche
print(f"|{texte:>10}|")              # Aligne a droite
print(f"|{texte:^10}|")              # Centre
input()














print("\nRemplissage avec des caracteres")
print(f"|{texte:*<10}|")
print(f"|{texte:*>10}|")
print(f"|{texte:*^10}|")
input()














print("\nEntiers avec des zeros")
print(f"Nombre : {nombre:05d}")       # 00042
input()














print("\nBases numeriques")
print(f"Decimal : {nombre:d}")
print(f"Binaire  : {nombre:b}")
print(f"Hexadecimal : {nombre:x}")
print(f"Octal : {nombre:o}")
input()














print("\nNotation scientifique")
grand_nombre = 123456789

print(f"{grand_nombre:e}")
print(f"{grand_nombre:.2e}")
input()














print("\nAfficher des accolades")
print(f"{{nom}} = {nom}")
print(f"{{age}} = {age}")
input()














print("\nDates")
from datetime import datetime

date = datetime.now()

print(f"Date : {date:%d/%m/%Y}")
print(f"Heure : {date:%H:%M:%S}")
print(f"Date et heure : {date:%d/%m/%Y a %H:%M:%S}")
input()














print("\nDebug rapide avec = ")
print(f"{nom=}")
print(f"{age=}")
print(f"{prix=:.2f}")
