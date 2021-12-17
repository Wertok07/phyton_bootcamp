def czy_pierwsza(a):
    if a == 2:
        return True
    if a % 2 == 0 or a <= 1:
        return False
    pierw = int(a ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if a % dzielnik == 0:
            return False
    return True


def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(11) is True


def test_czy_pierwsza_dla_liczby_nie_pierwszej():
    assert czy_pierwsza(9) == False  # nie używa się
    assert czy_pierwsza(9) is False  # id() is sprawdza czy id sa takie same i wartosci tez
    assert not czy_pierwsza(9)  # uzywa sie
