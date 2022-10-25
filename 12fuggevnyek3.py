def ellenorzottbeker(kerdes):
    while True:
        try:
            return int(input(kerdes))
        except ValueError:
            print("Nem szám!")

sz = ellenorzottbeker("Adj meg egy számot: ")
print("Elfogadva")
print(sz)