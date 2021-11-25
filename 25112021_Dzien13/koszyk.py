"""
Symulacja koszyka sklepu internetowego
"""

from product import Product
from basket import Basket

product1 = Product(1, "Pendrive", 69.99)
product2 = Product(2, "Słuchawka prysznicowa", 119.95)
product3 = Product(3, "Mysz ze skawiec", 299)

basket = Basket()

"""
TODO: Wykorzystać funkcje filter do znajdowania obiektu o wskazanym ID
"""


basket.add(product1, 6)
basket.add(product2, 2)
basket.add(product1, 3)
basket.add(product3, 1)
basket.remove(product2, 1)
basket.delete(product1)
print(f"Kwota za wszystkie produkty wynosi: {basket.get_total_amount()}zł")
basket.clear()
