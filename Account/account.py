class Account:

    def __init__(self, name, balance, pin, number):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.number = number

    def check_balance(self, pin):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount



