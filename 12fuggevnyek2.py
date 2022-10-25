from math import floor
import random
import time


def szerepel1(l, sz):
    for x in l:
        if x == sz:
            return True
    
    return False

def szerepel2(l, sz):
    for x in l:
        if x == sz:
            return True
        elif x > sz:
            return False
    
    return False



#teszteljünk
print("Lista megtöltése")
l = []
for x in range(1000000):
    l.append(random.randint(1, 9999999))

print("Lista megtöltve")
print("Rendezés")
l.sort()

print("Van-e benne 999998?")

print("1. módszer")
for x in range(19):
    szerepel1(l, 9)

if szerepel1(l, 9):
    print("Szerepel")
else:
    print("Nem szerepel")
print("2. módszer")
for x in range(19):
    szerepel2(l, 9)
    
if szerepel2(l, 9):
    print("Szerepel")
else:
    print("Nem szerepel")



