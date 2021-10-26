"""
Pierwsze liczby PG1
"""

while 1:
    m = int(input("Wpisz liczbe do sprawdzenia: "))
    if m > 1:
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
        if p == m:
            print(f"{p} jest lizcbą pierwszą")
            break
        lp = lp + 1
    p = p + 1
