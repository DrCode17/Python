t = [ 5, 3, 6, 2, 1, 9 ]
h = [5, 3, 1]

n = len(t)

for k in range(0, 3):
    lepes = h[k]
    for j in range(lepes, n):
        i = j - lepes
        kulcs = t[j]
        while i >= 0 and t[i] > kulcs:
            t[i+lepes] = t[i]
            i = i - lepes
        t[i+lepes] = kulcs

print(t)