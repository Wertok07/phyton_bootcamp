silnik = 10

def silnia(n):
    if n <= 1:
        return 1
    else:
        return n*silnia(n-1)

print(silnia(silnik), 3628800, end=" ")

def silnia2(n):
    wynik = 1
    for x in range(1, n+1):
        wynik *= x
    return wynik

print(silnia2(silnik))