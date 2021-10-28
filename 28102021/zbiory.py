# zbior = set([1,2,3,4])
# zbior2 = set([5,6,7,8])
#
# print(zbior, zbior2)
#
# zbior.add(3)
# zbior.add(7)
#
# print(zbior, zbior2)
# print()
# print(zbior | zbior2) # suma
# print(zbior & zbior2) # iloczyn
# print(zbior - zbior2) # roznica
# print(zbior2 - zbior)
# print(zbior ^ zbior2) # suma symetryczna -> suma - iloczyn

'''
Zadanie
'''
slownik = {}
slownik2 = {}
licznik = 0

liczby = input("Podaj szereg liczb odzielonych ',': ")

for znaki in liczby:
    licznik += 1
    if znaki == ",":
        continue
    slownik.setdefault(znaki, 0)
    znaki2 = int(znaki)
    if znaki2 > 1 and znaki2 < 101:
        if znaki2 == 2:
            slownik2.setdefault(licznik, 0)
        if znaki2 % 2:
            slownik2.setdefault(licznik, 0)

print("Unikalnych:", len(slownik.keys()))
print("parzystych w zakresie 2-100:", len(slownik2.keys()))
