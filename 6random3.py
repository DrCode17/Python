import random


szam = random.randint(1, 100)

for x in range(10):
    talalat = int(input("Tippelj egy számot! "))
    if talalat > szam:
        print("túl nagy")
    elif talalat < szam:
        print("túl kicsi")
    else:
        print("Eltaláltad")
        break
else:
    print("Nem találtad ki a számot. A szám a következő volt: "+ str(szam))

#else a for ciklus után akkor fut le, ha a for ciklus nem breakkel szakadt meg.