"""
Napisz funkcję tree wypisującą zawartość wskazanego katalogu w postaci drzewa katalogów i plików.
Napisz skrypt, który skorzysta z tej funkcji
Przykład użycia:
$ python tree.py .
.
|-- other
|    |-- create_emails.py
|    \-- create_logs.py
\-- README.md
Do wypisywania zawartości folderu można użyć funkcji scandir z moduły os
"""
import os

poziom = 0


def wypisywanie_folderow(sciezka):
    items = os.scandir(sciezka)
    itemslist = os.listdir(sciezka)
    for num, element in enumerate(items):
        if element.is_dir():
            drukowanie(element.name, sciezka.count("/"))
            path = sciezka + "/" + element.name
            wypisywanie_folderow(str(path))
        else:
            if num == len(itemslist) - 1:
                drukowanie(element.name, sciezka.count("/"), True)
            else:
                drukowanie(element.name, sciezka.count("/"))


def drukowanie(text, poz, item=False):
    if poz:
        print("|", end="")
        for p in range(0, poz):
            if poz > 1 and p < poz-1:
                print("    |", end="")
            else:
                print("    ", end="")
        if item:
            print("\--", text)
        else:
            print("|--", text)
    else:
        if item:
            print("\--", text)
        else:
            print("|--", text)


wypisywanie_folderow(".")
