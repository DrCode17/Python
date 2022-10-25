from ast import Delete
import random
with open("forrasok/gyakorinevek.txt") as f:
    nevek = [x.strip() for x in f.readlines()]
class harcos:
    def __init__(self) -> None:
        self.eletero = random.randint(90,120)
        self.tamadoero = random.randint(10, 20)
        self.nev = random.choice(nevek)
        self.kiesett = False
        self.legyozottek = 0
    
    def sebez(self, mennyit):
        if self.kiesett:
            raise AssertionError("Harcos már kiesett")
        self.eletero -= mennyit
        if self.eletero < 1:
            self.kiesett = True
            print(f"{self.nev}:\tKiestem!")
        else:
            print(f"{self.nev:10}:au! {self.eletero:3} életerőm maradt")

    def tamad(self, kit):
        if kit.kiesett:
            print(f"{self.nev:10}: {kit.nev} már kiesett! nem támadom meg")
            return
        print(f"{self.nev:10}: megtámadtam {kit.nev:10}-t {self.tamadoero:2} sebzéssel")
        kit.sebez(self.tamadoero)
        if kit.kiesett:
            self.legyozottek += 1
        
csapat1 = [harcos() for x in range(10)]
csapat2 = [harcos() for x in range(10)]

csapat1TamadoSorrend = list(csapat1)
random.shuffle(csapat1TamadoSorrend)
csapat2TamadoSorrend = list(csapat2)
random.shuffle(csapat2TamadoSorrend)

elok1 = list(csapat1)
elok2 = list(csapat2)
kijon = True
while len(elok1) != 0 and len(elok2) != 0:
    if kijon:
        kijon = not kijon
        if len(csapat1TamadoSorrend) == 0:
            csapat1TamadoSorrend = list(elok1)
            random.shuffle(csapat1TamadoSorrend)

        tamado1 = csapat1TamadoSorrend.pop(-1)

        tamado1.tamad(random.choice(elok2))
    else:
        kijon = not kijon
        if len(csapat2TamadoSorrend) == 0:
            csapat2TamadoSorrend = list(elok2)
            random.shuffle(csapat2TamadoSorrend)

        tamado2 = csapat2TamadoSorrend.pop(-1)

        tamado2.tamad(random.choice(elok1))

    elok1 = [x for x in csapat1 if not x.kiesett]
    elok2 = [x for x in csapat2 if not x.kiesett]



print("életbenmaradtak:")
print("csapat1:")
[print(x.nev) for x in elok1]
print("csapat2:")
[print(x.nev) for x in elok2]
print("\ntoplista:")
osszes = csapat1+csapat2
osszes.sort(reverse=True, key=lambda x: x.legyozottek)

[print(f"{x.nev}: {x.legyozottek}") for x in osszes[:5]]