def rosszrekurziv():
    rosszrekurziv()

def jorekurziv(melyseg):
    if melyseg > 5:
        return
    print(f"mélység: {melyseg}")
    jorekurziv(melyseg+1)
    jorekurziv(melyseg+1)

jorekurziv(1)