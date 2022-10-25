import random

l = []

szam = 1
while szam != 0:
    l.append(szam)
    szam = random.randint(0, 100)

print(l)