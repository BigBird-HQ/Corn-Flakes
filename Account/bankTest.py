import unittest

from Account.InsufficientFundsError import InsufficientFundsError
from Account.bank import Bank


class MyTestCase(unittest.TestCase):
    def test_that_customers_can_be_registered_in_the_bank(self):
        bank = Bank('mavericks')
        bank.register_customer('first_name', 'last_name', 'pin')
        self.assertEqual(1, bank.get_account())

    def test_that_account_can_be_found(self):
        bank = Bank('mavericks')
        found_account = bank.register_customer('first_name', 'last_name', 'pin')
        self.assertEqual(1, bank.get_account())
        self.assertEqual(found_account, bank.find_account(2))
        self.assertEqual('first_name last_name', found_account.get_name())

    def test_that_deposit_can_be_made(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        bank.deposit(account.get_number(), 2000)
        self.assertEqual(2000, account.get_balance())

    def test_that_amount_can_be_withdrawn(self):
        bank = Bank('mavericks')
        account = bank.register_customer('first_name', 'last_name', 'pin')
        bank.deposit(account.get_number(), 2000)
        with self.assertRaises(InsufficientFundsError):
            bank.withdraw(account.get_number(), 3000, 'pin')
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


if __name__ == '__main__':
    unittest.main()
