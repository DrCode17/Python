from while4Szavak import szavak
import random
from string import punctuation

szo = random.choice(szavak)
szo = "csalás"

del szavak

rejtszo = ""
hibak = 0
ismertBetuk = punctuation
nincsbenne = ""

while not (rejtszo == szo or hibak == 10):
    rejtszo = ""

    for x in szo:
        if x not in ismertBetuk:
            rejtszo = rejtszo+"_ "
        else:
            rejtszo = rejtszo + x + ""

    print(rejtszo)
    print("Tippjeid: " + nincsbenne)
    betu = input("Tippelj: ")[0]

    if betu in szo:
        ismertBetuk += betu
    else:
        nincsbenne += betu
        hibak += 1

if hibak == 10:
    print("Vesztettél! A szó: " + szo)
else:
    print("Kitaláltad!")

