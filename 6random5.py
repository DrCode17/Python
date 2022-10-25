from math import sqrt, ceil


meddig = int(input("Meddig szeretnéd megkeresni a prímeket? "))


print(2)
for vizsgaltSzam in range(3, meddig, 2):
    for osztoJelolt in range(2, ceil(sqrt(vizsgaltSzam - 1)), 1):
        if vizsgaltSzam % osztoJelolt == 0:
            break
    else:
        print(vizsgaltSzam)