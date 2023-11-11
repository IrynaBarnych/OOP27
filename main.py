# Завдання 2
# Розробіть систему управління замовленнями таксі. Кожне замовлення має містити інформацію про
# клієнта, адресу, тип автомобіля та вартість. Реалізуйте методи для додавання нових замовлень, зміни адреси та
# типу автомобіля, а також видалення замовлення.
# Використайте інкапсуляцію для захисту вартості від неправильних змін.

class Taxi:
    def __init__(self, client, adress, typ_auto, cost):
        self.__client = client
        self.__adress = adress
        self.__typ_auto = typ_auto
        self.__cost = cost

    def get_client(self):
        return self.__client

    def get_adress(self):
        return self.__adress

    def get_typ_auto(self):
        return self.__typ_auto

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return (f"Клієнт: {self.__client}. "
                f"Адреса: {self.__adress}. "
                f"Тип автомобіля: {self.__typ_auto}. "
                f"Вартість: {self.__cost} грн.")

    def change_client(self, new_client):
        self.__client = new_client

    def change_adress(self, new_adress):
        self.__adress = new_adress

    def change_typ_auto(self, new_typ_auto):
        self.__typ_auto = new_typ_auto

    def change_typ_cost(self, new_typ_cost):
        self.__cost = new_typ_cost

    def delete_order(self):
        print(f"Замовлення для клієнта {self.__client} видалено.")

    def new_order(self, client_n, adress_n, typ_auto_n, cost_n):
        self.__client = client_n
        self.__adress = adress_n
        self.__typ_auto = typ_auto_n
        self.__cost = cost_n
        print(f"Додано нове замовлення: {str(self)}")


taxi1 = Taxi("Шевченко Т.Г.", "вул. Економічна, буд.5", "Lanos", 150)
print(taxi1)
taxi2 = Taxi("Сковорода Г.С.", "вул. Незалежності, буд. 20", "Audi", 180)
print(taxi2)
taxi2.change_adress("вул. Нова, буд. 10")
taxi2.change_typ_auto("Mercedes")
taxi2.change_typ_cost(200)
print(f"Оновлена інформація: {taxi2}.")

taxi2.new_order("Пчілка О.", "вул. Вишнева, буд. 10", "Mercedes", 200)

taxi1.delete_order()







