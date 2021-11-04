"""
Dokumentowanie funkcji
"""


def delta(a: int, b: int, c: int) -> int:
    """
    Funkcja obliczająca delte dla równania kwadratowego
    :param a - wspl. A
    :param b - wspl. B
    :param c - wspl. C
    :return Zwraca wartość delty
    """
    return b ** 2 - (4 * a * c)


print(delta.__doc__)
print(delta(5, 4, 2))
