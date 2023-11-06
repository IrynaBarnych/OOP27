# рівні доступа

class MyClass:
    def __init__(self):
        self._protected_attribute = 10 #захищенний атрибут

    def _protected_method(self): #захищенний атрибут
        print("Це захищений метод")

class SubClass(MyClass):
    def access_protected(self):
        print(self._protected_attribute)
        self._protected_method()

a = MyClass
obj = SubClass()
print(dir(a))
print(obj._protected_attribute) #моветон
obj.access_protected()

#Рівень доступу Private (приватний)
class MyClass:
    def __init__(self):
        self.__private_attribute = 20

    def __private_method(self):
        print("Це приватний метод")

obj = MyClass()
#print(obj.__private_attribute)
#obj.__private_method()
print(dir(obj))
print(obj._MyClass__private_attribute)

#приклад з банком
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостатньо коштів на рахунку")

    def get_balance(self):
        return self._balance

# Використання:
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Результат: 1300