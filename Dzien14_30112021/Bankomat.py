class CashMachine:

    def __init__(self):
        self.cash_insite = []

    @property
    def is_available(self):
        if len(self.cash_insite):
            return True
        else:
            return False

    def put_money(self, list):
        for i in list:
            self.cash_insite.append(i)

    def withdraw_money(self, kwota):
        pomoc = kwota
        wyplata = []
        for papierek in sorted(self.cash_insite, reverse=True):
            if papierek <= pomoc:
                pomoc -= papierek
                wyplata.append(papierek)
        if sum(wyplata) == kwota:
            for papierek in wyplata:
                self.cash_insite.remove(papierek)
                return wyplata
        return []


cash_machine = CashMachine()
print(cash_machine.is_available)
cash_machine.put_money([200, 100, 100, 50])
print(cash_machine.is_available)
print(cash_machine.withdraw_money(150))
print(cash_machine.withdraw_money(102))
print(cash_machine.is_available)
print(cash_machine.withdraw_money(300))
print(cash_machine.withdraw_money(300))
print(cash_machine.is_available)