import random

szam = "".join(random.sample("0123456789", 4))

tipp = ""
tippszam = 0
while tipp != szam:
    tipp = input("\nTippelj egy számot: ")
    tippszam += 1

    benne = 0
    talalt = 0
    for x in range(4):
        if tipp[x] == szam[x]:
            talalt += 1
        elif tipp[x] in szam:
            benne += 1
    
    print("Teli találat: " + str(talalt))
    print("Van benne: " + str(benne))

print("Kitaláltad! " + str(tippszam) + " próbálkozás kellett csak")
