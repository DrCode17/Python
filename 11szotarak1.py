from pprint import pprint

f = open("forrasok/ajto.txt")

emberek = {}

for x in f.readlines():
    sorlista = x.split(" ")
    emberek[sorlista[2]] = sorlista[3]

pprint(emberek)

