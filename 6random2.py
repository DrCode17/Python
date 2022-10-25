from operator import ge
import random

jatekos = input("kő, papír, vagy olló?")
gep = random.choice(["kő", "papír", "olló"])

print("Te: " + jatekos)
print("Gép: " + gep)

if jatekos == gep:
    print("Döntetlen")

elif (jatekos == "kő" and gep == "olló") or (jatekos == "papír" and gep == "kő") or (jatekos == "olló" and gep == "papír"):
    print("Játékos nyert")
else:
    print("A gép nyert")