# int
# x = 1
# y = 2
# print(x+y)

# print(int(input("Podaj liczbe1:"))+int(input("Podaj liczbe2:")))
# y = input("Podaj liczbe2:")
# print(int(x)+int(y))

# # 1 Pobierz od uzytkownika imie i wzrost i wypisz na termianlu
# print("Imie: " + input("Podaj imie:") + ", Wzrost: " + input("Podaj wzrost:"))
#
# # 2 Zapytanie o dlugosc podstawy i wysokosc trojkata i wypisz
# pole = 0.5 * int(input("Podaj dlugosc podstawy trójkąta:")) * int(input("Podaj wysokość trójkąta:"))
# print(f"Pole trójkąta wynosi: {pole}")

a = input("Podaj miasto wyjazdu:")
b = input("Podaj miasto przyjazdu:")
c = input(f"Podaj dystans z {a} do {b}:")
d = input("Podaj cene paliwa za litr:")
e = input("Podaj spalanie na 100km:")
wynik = (float(c)/100)*(float(d)*float(e))
print(f"Koszt przejazdu {a}-{b} wynosi: {wynik:.2f}")

