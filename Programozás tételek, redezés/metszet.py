a = [ 5, 3, 6, 2, 1 ]
b = [ 6, 2, 7, 8, 9 ]
c = []
n = len(b)
for elem in a:
    i = 0
    while i < n and elem != b[i]:
        i+=1
    if i<n:
        c.append(elem)

print(c)