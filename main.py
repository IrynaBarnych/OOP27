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
    def display_items(self):
        for product, data in self.__items.items():
            print(f"товар: {product} {data['quanity']} шт ціна {data['price']}")

cart = ShoppingCart()
cart.add_items("Телефон", 2, 100)
cart.add_items("Книга", 3, 200)
cart.display_items()
print("Занальна вартість ", cart.calculate_total())

