# 2

class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_items(self, product, quanity, price):
        if product not in self.__items:
            self.__items[product] = {'quanity': quanity, 'price': price}
        else:
            self.__items[product]["quanity"] += quanity

    def calculate_total(self):
        total = 0
        for product, data in self.__items.items():
            total += data["quanity"] * data["price"]
            return total

