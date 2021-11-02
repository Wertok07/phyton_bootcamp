"""
Funkcja z parametrami domyslnymi
"""


def nowy_pracownik(imie, nazwisko, tel="22123456", email="email@firma.pl"):
    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "tel": tel,
        "email": email
    }
    return pracownik


# przykłady użycia
print(nowy_pracownik("Jan", "Kowalski", "601602603", "jkowalski@firma.com"))
print(nowy_pracownik("Zenon", "Nowak"))
print(nowy_pracownik("Ala", "Nowaczkiewicz", ))
print(nowy_pracownik("Marta", "Błoch"))
print(nowy_pracownik("Karta", "Włoch", email="kura@kfc.com"))
print(nowy_pracownik("Brunon", "Italy", email="kura@kfc.com", tel="74555"))
