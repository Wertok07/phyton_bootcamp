"""
Definiowanie klasy w pytongu
"""


class MojaKlasa:
    pass  # ta klasa nie robi nic


class Product:

    # pole statyczne
    product_counter = 0

    def __init__(self, id, name, price):  # konstruktor klasy
        Product.product_counter += 1
        self.id = id  # self.X tworzy pole X w klasie
        self.name = name
        self.price = price
        self.__password = "Qwerty123"
        self._protected = "123456"

    def get_info(self):
        return f"ID utworzonego produktu jest równe {self.id} a jej nazwa to {self.name} o cenie {self.price}zł"

    def get_info2(self):
        return f"{self.id} - {self.name} - {self.price}"

    def __str__(self):
        return self.get_info2()

    @staticmethod
    def len_():
        return Product.product_counter

    def clone(self):
        return Product(self.id, self.name, self.price)


#### Utworzenie obiektu klasy produkt

product1 = Product(24364536, "Wojtuś", 0.99)
print(product1.get_info())
print(product1.name)
print(product1.id)
print(product1._Product__password)
print(product1._protected)
# print(product1.__password)
print(product1)
print(Product.len_())
product2 = product1.clone()
print(Product.len_())
prod_list = []
for i in range(1, 11):
    prod = Product(i ** 2, f"Produkt-{i}", 5.99 + i * 0.1)
    prod_list.append(prod)

for x in prod_list:
    print(x)

print(Product.len_())
