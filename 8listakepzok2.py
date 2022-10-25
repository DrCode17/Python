import random

l = [random.randint(1, 6) for x in range(1000)]
l = [x for x in l if x != 2]

print(l)