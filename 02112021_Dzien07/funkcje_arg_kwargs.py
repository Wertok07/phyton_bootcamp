"""
Funkcje o dowolnej liczbie parametrów
"""


def wiele_parametrow(*args):
    suma = 0
    for arg in args:
        if type(arg) is int:
            suma += arg
    print(suma)


wiele_parametrow(1, "Ala ma kota", False, None, [], -1, 10, 56)


def min_dwa_parametry(jeden, dwa, *args):
    suma = 0
    for arg in args:
        if type(arg) is int:
            suma += arg
    print(suma)


min_dwa_parametry(1, "Ala ma kota", False, None, [], -1, 10, 56)

print("Ala ma kota", "Kot ma ale", [23, 52, 53, 4], sep="|", end="kot")
print("Ala ma kota", "Kot ma ale", [23, 52, 53, 4], sep="|")


# funkcja z kwargs

def funkcja_kwargs(**kwargs):
    print(f"imie: {kwargs.get('imie')}\nnazwisko: {kwargs.get('nazwisko')}\nwiek: {kwargs.get('wiek')}")

print("+"*50)
funkcja_kwargs(imie="Jan", nazwisko="Ponton", wiek=45, staz=56)

