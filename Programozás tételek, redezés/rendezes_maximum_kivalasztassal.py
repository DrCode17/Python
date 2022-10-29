t = [ 5, 3, 6, 2, 1, 9 ]
n = len(t)

for i in range(n-1, -1, -1):
    maxIndex = i
    for j in range(0, i):
        if(t[j] > t[maxIndex]):
            maxIndex = j
    tmp = t[i]
    t[i] = t[maxIndex]
    t[maxIndex] = tmp

print(t)