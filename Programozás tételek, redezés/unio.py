a = [ 5, 3, 6, 2, 1 ]
b = [ 6, 2, 7, 8, 9 ]

n = len(a)
m = len(b)

c = a.copy()

for j in range(0, m):
    i=0
    while i < n and b[j] != a[i]:
        i+=1
    if i>=n:
        c.append(b[j])

print(c)