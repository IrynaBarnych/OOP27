# Завдання 1
# Створіть систему управління замовленнями готелю. Кожне замовлення має містити інформацію
# про клієнта, тип кімнати, кількість днів проживання та вартість. Реалізуйте методи для додавання замовлення,
# зміни типу кімнати та кількості днів, а також видалення замовлення. Використайте інкапсуляцію для
# захисту вартості від неправильних змін.

class Hotel:
    def __init__(self, client, typ_room, days, cost):
        self.__client = client
        self.__typ_room = typ_room
        self.__days = days
        self.__cost = cost

    def get_client(self):
        return self.__client

    def get_typ_room(self):
        return self.__typ_room

    def get_days(self):
        return self.__days

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return (f"Клієнт: {self.__client}. "
                f"Тип кімнати: {self.__typ_room}. "
                f"Кількість днів: {self.__days} дні."
                f" Вартість: {self.__cost} грн./добу")

    def change_typ_room(self, new_typ_room):
        self.__typ_room = new_typ_room

    def change_days(self, new_days):
        self.__days = new_days

    def change_cost(self, new_cost):
        self.__cost = new_cost

    def delete_order(self):
        print(f"Замовлення для клієнта {self.__client} видалено.")


hotel1 = Hotel("Шевченко Т.Г.", "економ", 2, 1500)
print(hotel1)
hotel2 = Hotel("Сковорода Г.С.", "студія", 5, 1800)
print(hotel2)

# Змінимо тип кімнати та вартість
hotel1.change_typ_room("стандарт")
hotel1.change_cost(2000)
print(f"Оновлена інформація: {hotel1}.")
hotel2.change_typ_room("люкс")
hotel2.change_cost(10000)
hotel2.change_days(5)
print(f"Оновлена інформація: {hotel2}.")

hotel1.delete_order()







