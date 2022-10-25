
while True:
    try:
        szam = int(input("Adj meg egy számot: "))
    except ValueError:
        print("Nem egy szám!")

print(szam * 2)
