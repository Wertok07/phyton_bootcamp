"""
Pierwsze liczby PG1
"""
def liczba_pierwsza(a):
    if a == 2:
        return True
    if a % 2 == 0 or a <= 1:
        return False
    pierw = int(a ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if a % dzielnik == 0:
            return False
    return True

while 1:
    m = int(input("Wpisz liczbe do sprawdzenia: "))
    if m > 1:
        break
if liczba_pierwsza(m) is True:
    print(f"{m} jest lizcbą pierwszą")
if liczba_pierwsza(m) is False:
    print(f"{m} nie jest lizcbą pierwszą")

t = True
lp = 0
d = 2
p = 2
n = 1000
while lp < n:
    while d < p:
        if p % d == 0:
            t = False
            break
        d = d + 1
    if t:
        #print(p)
        if p == m:
            print(f"{p} jest lizcbą pierwszą")
            break
        lp = lp + 1
    p = p + 1