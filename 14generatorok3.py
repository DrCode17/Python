def fibonacciGenerator(mennyit):
    yield 1
    yield 1
    
    elozo = 1
    elozoElotti = 1
    for x in range(mennyit):
        jelenlegi = elozo + elozoElotti
        yield jelenlegi
        elozoElotti = elozo
        elozo = jelenlegi

for x in fibonacciGenerator(100):
    print(x)