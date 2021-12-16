import json

lista = []
slownik = {}

try:
    with open("zadanie_1_dane.json", "r") as f:
        lista = json.load(f)
except FileNotFoundError:
    pass

komenda = input("Co chcesz zrobić? [d - dodaj, w - wypisz]")

if komenda == "d":
    slownik["v1"] = input("Imię: ")
    slownik["v2"] = input("Nazwisko: ")
    slownik["v3"] = input("Rok urodzenia: ")
    slownik["v4"] = input("Pensja: ")
    # slownik = {
    #     "v1": input("Imię: "),
    #     "v2": input("Nazwisko: "),
    #     "v3": input("Rok urodzenia: "),
    #     "v4": input("Pensja: ")
    # }
    lista.append(slownik)

    with open("zadanie_1_dane.json", "w") as f:
        json.dump(lista, f)


elif komenda == "w":
    for nr, listafor in enumerate(lista, start=1):
        print(nr, "Imię i nazwisko:", listafor["v1"], listafor["v2"],"Rok urodzenia:", listafor["v3"],"Pensja:", listafor["v4"])
else:
    print("Nie umiesz czytać, idź do przedszkola :(")

