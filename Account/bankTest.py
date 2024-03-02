import unittest

from Account.InsufficientFundsError import InsufficientFundsError
from Account.InvalidAmountError import InvalidAmountError
from Account.bank import Bank


class MyTestCase(unittest.TestCase):
    def test_that_customers_can_be_registered_in_the_bank(self):
        bank = Bank('mavericks')
        bank.register_customer('first_name', 'last_name', 'pin')
        self.assertEqual(1, bank.get_account())

    def test_that_more_than_one_customer_can_be_registered(self):
        bank = Bank('mavericks')
        bank.register_customer('first_name', 'last_name', 'pin')
        bank.register_customer('first_name1', 'last_name1', 'pin')
        self.assertEqual(2, bank.get_account())

    def test_that_account_can_be_found(self):
        bank = Bank('mavericks')
        found_account = bank.register_customer('first_name', 'last_name', 'pin')
        self.assertEqual(1, bank.get_account())
        self.assertEqual(found_account, bank.find_account(1))
        self.assertEqual('first_name last_name', found_account.get_name())

    def test_that_positive_amount_can_be_deposited(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        bank.deposit(account.get_number(), 2000)
        self.assertEqual(2000, account.get_balance())

    def test_that_negative_amount_cannot_be_deposited_raise_exception(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        with self.assertRaises(InvalidAmountError):
            bank.deposit(account.get_number(), -2000)
        self.assertEqual(0, account.get_balance())

    def test_that_zero_amount_cannot_be_deposited_raise_exception(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        with self.assertRaises(InvalidAmountError):
            bank.deposit(account.get_number(), 0)
        self.assertEqual(0, account.get_balance())

    def test_that_positive_amount_can_be_withdrawn(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        bank.deposit(account.get_number(), 2000)
        bank.withdraw(account.get_number(), 1000, 'pin')
        self.assertEqual(1000, account.get_balance())

    def test_that_amount_bigger_than_account_balance_cannot_be_withdrawn_raise_exception(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        bank.deposit(account.get_number(), 2000)
        with self.assertRaises(InsufficientFundsError):
            bank.withdraw(account.get_number(), 3000, 'pin')
        self.assertEqual(2000, account.get_balance())

    def test_that_negative_amount_cannot_be_withdrawn_raise_exception(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        bank.deposit(account.get_number(), 2000)
        with self.assertRaises(InvalidAmountError):
            bank.withdraw(account.get_number(), -2000, 'pin')
        self.assertEqual(2000, account.get_balance())

    def test_that_balance_can_be_checked(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        bank.check_balance(account.get_number(), 'pin')
        self.assertEqual(0, account.get_balance())

    def test_that_account_can_be_removed(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        self.assertEqual(1, bank.get_account())
        bank.remove_account(account.get_number(), 'pin')
        self.assertEqual(0, bank.get_account())

    def test_transfers_between_two_accounts_in_the_same_bank(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        account1 = bank.register_customer('first_name1', 'last_name', 'pin')
        bank.deposit(1, 5000)
        bank.transfer(1, 2, 2000, 'pin')
        self.assertEqual(3000, account.get_balance())
        self.assertEqual(2000, account1.get_balance())


if __name__ == '__main__':
    unittest.main()
