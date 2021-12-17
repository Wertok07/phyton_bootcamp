import pickle

lista = ['1',"2",'3']

class Car:

    def __init__(self, name):
        self.name = name

car = Car("Merol")
#car.model = "w123"

with open("mojedane.pickle", "wb") as f:
    pickle.dump(car, f)


with open("mojedane.pickle", "rb") as f:
    dane = pickle.load(f)

print(dane)