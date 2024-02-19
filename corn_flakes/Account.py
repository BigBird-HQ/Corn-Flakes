from decimal import Decimal


class Account:
    def __init__(self, name, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self, amount):
        if amount < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self.balance = amount

    def __str__(self):
        return f"Name {self.name} Balance: {self.balance}"


a1 = Account('Dayo', Decimal(10))

print(a1)
