from orderitem import OrderItem


class Basket:
    '''Klasa opisująca koszyk zamówienia/liste pozycji zamówienia'''

    def __init__(self):
        self.items = []

    def clear(self):
        '''Czyści zawartość koszyka'''
        self.items.clear()

    def get_total_amount(self):
        '''Zwraca kwote za wszystko w koszyku'''
        fullCost = 0
        for it in self.items:
            fullCost += it.product.price * it.qnty
        return fullCost

    def add(self, product, qnty):
        '''Dodaje/edytuje pozycje zamowienia dla podanego produktu'''
        new_item = OrderItem(product, qnty)
        for it in self.items:
            if it.product.id == new_item.product.id:
                it.qnty += qnty
                return
        self.items.append(new_item)

    def remove(self, product, qnty):
        '''Usuwa pozycje zamowienia dla podanego produktu'''
        for it in self.items:
            if it.product.id == product.id:
                it.qnty -= qnty
                return

    def delete(self, product):
        '''Usuwa pozycje zamowienia dla podanego produktu'''
        for index, it in enumerate(self.items):
            if it.product.id == product.id:
                self.items.remove(it)
                # self.items.pop(index) # Tak też można
                return
