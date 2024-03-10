from Account.InsufficientFundsError import InsufficientFundsError
from Account.InvalidAmountError import InvalidAmountError
from Account.InvalidPinError import InvalidPinError


class Account:

    def __init__(self, name, pin, number):
        self.name = name
        self.balance = 0
        self.pin = pin
        self.number = number

    def check_balance(self, pin):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError('Invalid Amount')
        self.balance += amount

    def withdraw(self, amount, pin):
        self.insufficient_funds(amount)
        self.invalid(amount)
        self.validate(pin)
        self.balance -= amount

    def validate(self, pin):
        if not self.pin == pin:
            raise InvalidPinError('Invalid Pin')

    def invalid(self, amount):
        if amount <= 0:
            raise InvalidAmountError('Invalid Amount')
        return True

    def insufficient_funds(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError('Insufficient Funds')

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number
