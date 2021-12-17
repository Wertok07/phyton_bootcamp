#Zadanie_1

Zaimplementuj klasy odpowiedzialne za tworzenie dokumenty w składni MarkDown:
* Stwórz klasę bazową Element zawierającą podstawową implementację metody render() oraz kilka jej klas pochodnych.
* Stwórz klasę Document umożliwiającą wyrendorowanie dodanych elementów.

Przykład użycia:
'''
    >>> document = Document() document.add_element(HeaderElement('Header'))
    >>> document.add_element(LinkElement('ABC', 'abc.com'))
    >>> document.add_element(Element('Simple'))
    >>> document.render()
    Header
    ======
    (ABC)[http://abc.com]
    Simple
'''

Metoda klasowa, metoda statyczna

Moduły

Zadanie

Utwórz następującą strukturę pakietów i modułów:

główny pakiet mathematica
pakiet wewnętrzny geometry
moduł figures w pakiecie geometry z funkcjami square_area oraz triangle_area
pakiet wewnętrzny algebra
moduł matrices w pakiecie algebra z funkcją add_matrices i sub_matrices
główny pakiet tests
moduł test_geometry testujący funkcje geometryczne
moduł test_algebra testujący funkcje algebraiczne
Biblioteka Standardowa

json

Napisz program obsługujący bazę danych pracowników. W bazie danych przechowuj imię, nazwisko, email, rok urodzenia, pensję. Skorzystaj z modułu json. Przykład użycia:

$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] d
Imie: Jan
Nazwisko: Nowak
Rok urodzenia: 1980
Pensja: 5000.0
$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] w
Pracownicy:
- [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN