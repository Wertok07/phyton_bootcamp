silnik = 300


def silnia(n):
    if n <= 1:
        return 1
    else:
        return n * silnia(n - 1)


#print(silnia(silnik), 3628800, end=" ")


def silnia2(n):
    wynik = 1
    for x in range(1, n + 1):
        wynik *= x
    return wynik


#print(silnia2(silnik))

# Badanie szybkości wykonania funkcji
import time

t1 = time.time()  # zwraca unix time
for _ in range(0, 10_000):
    silnia(silnik)
t2 = time.time()

print("Rekurencja:", t2 - t1)

t3 = time.time()  # zwraca unix time
for _ in range(0, 10_000):
    silnia2(silnik)
t4 = time.time()

print("Iteracja:", t4 - t3)
