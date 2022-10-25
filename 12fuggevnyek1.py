def fakt(szam):
    eredmeny = 1
    for i in range(1, szam+1):
        eredmeny *= i

    return eredmeny

print(fakt(5))