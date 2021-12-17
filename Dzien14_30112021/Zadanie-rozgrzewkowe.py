"""
Zadanie rozgrzewkowe
"""


class Car:

    def __init__(self, level):
        self.level = level

    def drive(self, level):
        if self.level >= level:
            self.level -= level
            print("Pozostało:", self.level)
        else:
            print("Nie masz baterii")

    def charge(self):
        self.level += 100


car = Car(100)

car.drive(70)
car.drive(50)
car.drive(50)
car.charge()
car.drive(50)

