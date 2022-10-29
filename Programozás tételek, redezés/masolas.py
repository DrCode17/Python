a = [ 3, 8, 2, 4, 5, 1, 6]
b = []

def dupla(num):
    return num * 2

for elem in a:
    b.append(dupla(elem))

print(b)