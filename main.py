# Завдання 3
# Створіть клас "Електронний Гаманець" додавши можливість видаляти та додавати гроші, а також перевіряти
# баланс.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума виведення повинна бути більше нуля.")
        elif amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостатньо коштів на рахунку")

    def get_balance(self):
        return self._balance


account = BankAccount(500)
account.deposit(10000)
account.withdraw(200)

print(f"Баланс: {account.get_balance()} грн.")
account.deposit(100)
print(f"Депозит: {account.get_balance()} грн.")
account.withdraw(50)
print(f"Баланс після виведення: {account.get_balance()} грн.")


