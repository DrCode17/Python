

from math import floor


meddig=int(input("Melyik számnak szeretnéd az osztóit? "))

#Leglassabb változat:
for x in range(1, meddig):
    if meddig%x == 0:
        print(x)

#egyel gyorsabb változat
for x in range(1, floor(meddig/2)):
    if meddig%x == 0:
        print(x)