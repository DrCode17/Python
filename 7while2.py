from operator import ge, truediv
import random



while True:
    jatekos = input("kő, papír, vagy olló?")
    gep = ["kő", "papír", "olló"][random.randint(0, 2)]

    print("Te: " + jatekos)
    print("Gép: " + gep)

    if jatekos == gep:
        print("Döntetlen")

    elif (jatekos == "kő" and gep == "olló") or (jatekos == "papír" and gep == "kő") or (jatekos == "olló" and gep == "papír"):
        print("Játékos nyert")
    else:
        print("A gép nyert")
    

    if input("Újrapróbálod? ") != "igen":
        break