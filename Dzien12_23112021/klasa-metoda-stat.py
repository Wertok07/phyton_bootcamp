"""
Metoda statyczna: można wywołać bez konieczności tworzenia instancji danego obiektu
"""


class Planimetria:

    def calc_squere_area(self, a):
        return a ** 2


class PlanimetriaStatic:

    @staticmethod
    def calc_squere_area(a):
        return a ** 2


p = Planimetria().calc_squere_area(6)
print(p)

print(PlanimetriaStatic.calc_squere_area(6))
