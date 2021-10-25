"""
Pierwsze liczby PG1
"""

while 1:
    n = int(input("Wpisz liczbe do sprawdzenia: "))
    if n > 1:
        break

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
        if m == lp:
            print(f"{m} jest lizcbą pierwszą")
            break
        lp = lp + 1
    p = p + 1
