class Capa:
    elohely="óceán"
    allatfaj = "hal"

    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

    def uszas(self):
        if self.allatfaj == "hal":
            print(f"{self.nev} úszik")
        else:
            print(f"{self.nev} csak vergődik, mert nem hal")

    def elvarazsol(self, mive):
        self.allatfaj = mive
        print("Abrakadabra")

    def idose(self):
        if self.kor > 20:
            print(f"{self.nev} idős")
        else:
            print(f"{self.nev} nem idős")

boldizsar = Capa("Boldizsár", 5)
boldizsar.idose()
boldizsar.uszas()
boldizsar.elvarazsol("macska")
boldizsar.uszas()