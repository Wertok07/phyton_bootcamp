"""
Zadanie domowe
"""


class RegisterWork:
    cash = 0

    def __init__(self, rate): # blokada na najniższą krajową
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
            RegisterWork.cash += self.rate * time
        else:
            print("Zły czs XD")

    def pay(self):
        print(f"Wypłata wynosi {RegisterWork.cash}zł")
        RegisterWork.cash = 0


work = RegisterWork(100)
work.register_time(5)
work.register_time(2.5)
work.pay()
work.register_time(8)
work.pay()
