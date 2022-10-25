from math import ceil, sqrt


def primek(meddig):
    yield 2

    for vizsgaltSzam in range(3, meddig, 2):
        for osztoJelolt in range(2, ceil(sqrt(vizsgaltSzam - 1)), 1):
            if vizsgaltSzam % osztoJelolt == 0:
                break
        else:
            yield vizsgaltSzam

for x in primek(1000):
    print(x)