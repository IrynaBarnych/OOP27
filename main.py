# Завдання 1

#Рівень доступу приватний
class User:
    def __init__(self, name, age, email):
        self._name = name
        self.__age = age
        self.__email = email


    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email


user1 = User("Ivan", 19, "example@gmail. com")
print(user1.get_name())
print(user1.get_age())
print(user1.get_email())