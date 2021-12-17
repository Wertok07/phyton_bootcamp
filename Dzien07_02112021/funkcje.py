"""
Funkcje w pythonie
"""
import math


# pusta funkcja
def foo():
    pass  # Zamiast None, pustka.


foo()


# Funkcja do obliczania pola koła
def oblicz_pole(r):
    # pole = math.pi * (r ** 2)
    # return pole
    return math.pi * (r ** 2)


print(f'Pole koła wynosi: {oblicz_pole(2)}')


# Funkcja do obliczania obwód koła
def oblicz_obwod(r):
    return 2 * math.pi * r


print(f'Obwód koła wynosi: {oblicz_obwod(2)}')


# Funkcja do obliczania pola i obwodu koła
def oblicz_kolo(r):
    return oblicz_pole(r), oblicz_obwod(r)


print(f'Pole oraz obwód koła wynosi: {oblicz_kolo(3)}')


# funkcja która nie zwraca wartości
def wypisz_duze_litery(s):
    return print(s.upper())


wypisz_duze_litery('ala ma kota')