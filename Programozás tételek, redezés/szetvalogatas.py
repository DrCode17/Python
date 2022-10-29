a = [ 3, 8, 2, 4, 5, 1, 6]
b = []
c = []

for elem in a:
    if elem < 5:
        b.append(elem)
    else:
        c.append(elem)

print(b)
print(c)