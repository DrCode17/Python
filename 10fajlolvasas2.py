f = open("forrasok/ajto.txt")

for x in f.readlines():
    print(x.strip())

f.close()
#strip() azért kell, mert a readlines() rajtahagyta a sorokon a \n karaktert
