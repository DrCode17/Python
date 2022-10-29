t = [ 5, 3, 6, 2, 1 ]
n = len(t)

for i in range(0, n-1):
    for j in range(i+1, n):
        if(t[i] > t[j]):
            tmp = t[i]
            t[i] = t[j]
            t[j] = tmp

print(t)