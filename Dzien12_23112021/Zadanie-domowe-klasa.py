"""
Zadanie domowe
"""


class RegisterWork:

    def __init__(self, rate): # blokada na najniższą krajową
        self.cash = 0
        if type(rate) is int:
            if rate > 19:
                self.rate = rate
            else:
                print("Kwota została ustawiona na 19zł/h, bo mnije to nielegalne")
                self.rate = 19
        else:
            print("Nie podałeś liczby, przyjąłem 19zł, szefie")
            self.rate = 19

    def register_time(self, time):  # czas w godzinach blokada na ujemny czas
        if time > 0:
            self.cash += self.rate * time
        else:
            raise ValueError("Zły czs XD") # wyjątek

    def pay(self):
        print(f"Wypłata wynosi {self.cash}zł")
        self.cash = 0


work = RegisterWork(100)
work2 = RegisterWork(80)
work.register_time(5)
work2.register_time(5)
work.register_time(2.5)
work.pay()
work2.register_time(8)
work2.pay()
