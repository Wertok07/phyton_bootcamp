def wicej_niz(text, li):
    slo = dict()
    ss = set()
    text = text.replace(" ", "")
    for litera in text:
        litera = litera.lower()
        slo.setdefault(litera, 0)
        slo[litera] += 1
    for k, val in slo.items():
        if val >= li:
            ss.add(k)
    return ss


print(wicej_niz("Ala ma kota", 3))
print(wicej_niz("y", 1))


def test_jeden():
    assert wicej_niz("Ala ma kota", 3) == set("a")
    assert wicej_niz("Ala ma kota", 1) == {'o', 'm', 't', 'k', 'a', 'l'}
    assert wicej_niz("y", 1) == set("y")
