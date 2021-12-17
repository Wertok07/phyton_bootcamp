"""
Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami. Znaki pomiędzy którymi ma odbywać się zliczanie powinny być argumentami z wartościami domyślnymi ‐ odpowiednio < i > . Nawiasy mogę być zagnieżdżone i mogą wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.
Przykład użycia:
>> policz_znaki('ala ma <kota> a kot ma ale') = 4
>> policz_znaki('ala ma [kota [a kot]] ma [ale]', '[', ']') = 18
>> policz_znaki('a <a<a<a>>>') = 6
"""


def policz_znaki2(text, o="<", c=">"):
    stri = ""

    start = set()
    stop = set()

    for txt in range(0, len(text)):
        if text[txt] == o:
            start.add(txt)
        if text[txt] == c:
            stop.add(txt)
    print(start)
    print(stop)
    start = sorted(start)
    stop = sorted(stop)
    print(start)
    print(stop)

    for ii, tt in enumerate(range(start, stop)):
        if ii == 0:
            continue
        stri = stri + text[tt]
    if (stri.find(o) != 0) and (stri.find(o) != 0):
        return len(stri)
    else:
        dl = policz_znaki(stri, o, c)
        return len(stri) + dl


def policz_znaki(tekst, start="<", stop=">"):
    licznik = 0
    poziom = 0
    for znak in tekst:
        if znak == start:
            poziom += 1
        elif znak == stop:
            poziom -= 1
        else:
            licznik += poziom
    return licznik


print(policz_znaki('ala ma [kota [a kot]] ma [ale]', '[', ']'))


def test_funkcji():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('a <a<a<a>>>') == 6


def test_policz_znaki_dla_pustego_napisu():
    assert policz_znaki("") == 0


def test_policz_znaki_jeden_poziom():
    assert policz_znaki("<a>") == 1


def test_policz_znaki_wiele_poziomow():
    assert policz_znaki("<<a>>") == 2
    assert policz_znaki("<a<a>>") == 3
    assert policz_znaki("<a<b<c>>>") == 6


def test_policz_znaki_niestandardowe_znaczniki():
    assert policz_znaki("<a<b<c>>>", "[", "]") == 0
    assert policz_znaki("[a[b[c]]]", "[", "]") == 6
