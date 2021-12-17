import datetime

rok = datetime.datetime.now().year
class Osoba:

    def __init__(self, imie: str, rok_ur: int):
        self.imie = imie
        self.rok_ur = rok_ur

    @property
    def wiek(self):
        return rok - self.rok_ur