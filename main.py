# 2

class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_items(self, product, quanity, price):
        if product not in self.__items:
            self.__items[product] = {'quanity': quanity, 'price': price}
        else:
            self.__items[product]["quanity"] += quanity

