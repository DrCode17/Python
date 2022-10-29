t = [ 5, 3, 6, 2, 1, 9 ]
n = len(t)

for i in range(0, n-2):
    minIndex = i
    for j in range(i+1, n-1):
        if(t[j] < t[minIndex]):
            minIndex = j
    if minIndex != i:
        tmp = t[i]
        t[i] = t[minIndex]
        t[minIndex] = tmp

print(t)