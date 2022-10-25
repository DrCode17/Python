import random

f = open("forrasok/randomszamok.txt", "w+")

for x in range(100):
    f.write(str(random.randint(1, 100))+ "\n")

#alternatív megoldás
for x in range(100):
    print(random.randint(1, 100), file=f)

f.close()