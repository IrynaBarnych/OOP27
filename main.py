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

    def get_client (self):
        return self.__client

    def get_typ_room(self):
        return self.__typ_room

    def get_days (self):
        return self.__days

    def get_cost(self):
        return self.__cost

    def display_info(self):
        print(f"Інформація про клієнта: {self.__client}")
        print(f"Тип кімнати: {self.__typ_room} ")
        print(f"Кількість днів: {self.__days}")
        print(f"Вартість: {self.__cost} грн.")

# Приклад використання
hotel1 = Hotel("Шевченко Т.Г.", "економ", 2, 1500 )
hotel1.display_info()

# Використовуємо методи для отримання даних
print(f"Інформація про клієнта: {hotel1.get_client()}")
print(f"Тип кімнати: {hotel1.get_typ_room()}")
print(f"Кількість днів: {hotel1.get_days()}")
print(f"Вартість: {hotel1.get_cost()} грн.")






