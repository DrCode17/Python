from pprint import pprint
import re

with open("forrasok/JanosVitez.txt") as f:
    szoveg = f.read()
    szolista = szoveg.split()
    szavakSzama = {}
    for x in szolista:
        try:
            szavakSzama[x] += 1
        except KeyError:
            szavakSzama[x] = 1

l = list(szavakSzama.items())

def ezalapjan(egybejegyzes):
    return egybejegyzes[1]

l.sort(key=ezalapjan, reverse=True)
pprint(l)