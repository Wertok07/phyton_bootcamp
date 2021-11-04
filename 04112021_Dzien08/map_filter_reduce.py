"""
map - mapowanie danych
filter - filtrowanie danych
reduce - konsolidacja danych
"""

lista = [5, -2, 8, 9, 33, 10]
# podejscie klasyczne
lista_results = []
for x in lista:
    lista_results.append(x ** 2)

print(lista, lista_results, sep="\n")


def kwadrat(x):
    return x ** 2


# uzycie funkcji map()
lista2 = list(map(kwadrat, lista))
print(lista2)

# uzycie funkcji anonimowej lambda
lista_res = list(map(lambda x: x ** 2, lista))
print(lista_res)

# użycie funkcji filter()
lista_res = []
for x in lista:
    if x > 0:
        lista_res.append(x)

print(lista_res)


def wieksze_niz_0(x):
    return x > 0


druk = list(filter(lambda x: x > 0, lista))
print(druk)

# użycie funkcji reduce
import functools

lista = [1, 2, 3, 4, 5]
print(sum(lista))

print(functools.reduce(lambda x, y: x * y, lista))
