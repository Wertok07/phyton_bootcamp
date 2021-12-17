"""

listy w pytonie

"""

lists1 = list() # pusta lista
lists1 = [] # pusta lista
lista1 = [1, 2, "Ala ma kota", True, 999.99, (200,), ["a", "b", "c"], None]
print(lista1)
lista1.append("dolaczam")
print(lista1)
lista1.extend([9,8,7,1])
print(lista1)
# Wstawianie elementu w listę
lista1.insert(3, "a kot ma Ale")
print(lista1)
# Usuwanie elementu z listy
lista1.remove("Ala ma kota")
print(lista1)
lista1.remove(1)
print(lista1)
print(lista1.count(1))
print(f"Długość listy: {len(lista1)}")
if lista1.count("Ala ma kota"):
    lista1.remove("Ala ma kota")
if "Ala ma kota" in lista1:
    lista1.remove("Ala ma kota")
print(lista1)
print(f"Pozycja liczby 999.99: {lista1.index(999.99)}")
# usuwanie 1 elementu na liscie
del(lista1[0])
print(lista1)
# modyfikacja wartosci elementu listy
lista1[0] = "jkhgidsk"
print(lista1)

# kopiowanie list
lista2 = lista1.copy()

print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")
lista2[0] = 5
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")
print(lista2[0])

print(f"Lista1 = {id(lista1)}")
print(f"Lista2 = {id(lista2)}")
