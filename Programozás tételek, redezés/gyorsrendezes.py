t = [ 5, 3, 6, 2, 1, 9 ]

def gyorsrendezes(lista):
    meret = len(lista)
    if meret <= 1:
        return lista
    kicsik = []
    egyenlo = []
    nagyok = []
    pivot = lista[meret-1]
    for num in lista:
        if num < pivot:
            kicsik.append(num)
        if num == pivot:
            egyenlo.append(num)
        if num > pivot:
            nagyok.append(num)
    return gyorsrendezes(kicsik) + egyenlo + gyorsrendezes(nagyok)

print(gyorsrendezes(t))