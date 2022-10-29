t = [ 5, 3, 6, 2, 1, 9 ]
n = len(t)

for i in range(0, n):
    kulcs = t[i]
    j = i - 1
    while j >= 0 and t[j] > kulcs:
        t[j+1] = t[j]
        j = j - 1
    t[j+1] = kulcs

print(t)