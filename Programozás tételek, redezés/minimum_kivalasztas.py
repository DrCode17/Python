t = [ 5, 3, 6, 2, 1 ]

minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)