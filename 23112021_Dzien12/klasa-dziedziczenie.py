"""
Dziedziczenie
"""


class Parent:

    def metoda1(self):
        print("Parent - metod1")

    def metoda2(self):
        print("Parent - metod2")


class Child(Parent):

    def metoda1(self):
        super(Child, self).metoda1()
        print("Child - metod1")


p = Parent()
c = Child()

p.metoda2()
p.metoda1()
c.metoda1()
c.metoda2()
