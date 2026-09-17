# Les operateurs en Python

a = 10
b = 3

print("Operateurs arithmetiques")

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)
input()










print("\noperateurs de comparaison")

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
input()










print("\noperateurs logiques")

x = True
y = False

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)
input()










print("\noperateurs d'affectation")

n = 10

print("n =", n)

n += 5
print("n += 5  ->", n)

n -= 3
print("n -= 3  ->", n)

n *= 2
print("n *= 2  ->", n)

n /= 4
print("n /= 4  ->", n)

n //= 2
print("n //= 2 ->", n)

n %= 3
print("n %= 3  ->", n)

n **= 2
print("n **= 2 ->", n)
input()










print("\noperateurs bit a bit")

a = 10
b = 3

print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~a     =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
input()










print("\noperateurs d'appartenance")

liste = [1, 2, 3, 4, 5]

print("3 in liste      :", 3 in liste)
print("10 in liste     :", 10 in liste)
print("10 not in liste :", 10 not in liste)
input()










print("\noperateurs d'identite")

objet1 = [1, 2, 3]
objet2 = objet1
objet3 = [1, 2, 3]

print("objet1 is objet2     :", objet1 is objet2)
print("objet1 is objet3     :", objet1 is objet3)
print("objet1 is not objet3 :", objet1 is not objet3)
input()










print("\noperateurs avec des chaines")
prenom = "alice"

nom = "dupont"

print("concatenation :", prenom + " " + nom)
print("repetition    :", prenom * 3)
print("alice" in prenom)
print("bob" not in prenom)

print("\noperateur ternaire")

age = 20
message = "majeur" if age >= 18 else "mineur"

print(message)
input()








print("\noperateur walrus :=")
if (longueur := len("python")) > 5:
    print("le mot contient", longueur, "caracteres.")
