from Account.InvalidAmountError import InvalidAmountError


class Account:

    def __init__(self, name, balance, pin, number):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.number = number

    def check_balance(self, pin):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError('Invalid Amount')
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount



