import unittest

from Account.account import Account


class MyTestCase(unittest.TestCase):
    def test_that_account_is_empty_at_creation(self):

        account = Account('mavericks', 0, '1234', 1)

        self.assertEqual(0, account.check_balance('1234'))

    def est_that_balance_increases_when_positive_amount_is_deposited(self):
        account = Account('mavericks', 0, '1234', 1)
        account.deposit(0)
        self.assertEqual(0, account.check_balance('1234'))

    def test_that_positive_amount_amount_can_be_deposited(self):
        account = Account('mavericks', 0, '1234', 1)
        account.deposit(2000)
        self.assertEqual(2000, account.check_balance('1234'))

    def test_that_balance_increases_when_positive_amount_is_deposited_twice(self):
        account = Account('mavericks', 0, '1234', 1)
        account.deposit(2000)
        account.deposit(3000)
        self.assertEqual(5000, account.check_balance('1234'))

    def test_that_balance_decreases_when_positive_amount_is_withdrawn(self):
        account = Account('mavericks', 0, '1234', 1)
        account.deposit(5000)
        account.withdraw(3000)
        self.assertEqual(2000, account.check_balance('1234'))

    def test_that_balance_remains_unchanged_when_zero_amount_is_withdrawn(self):
        account = Account('mavericks', 0, '1234', 1)
        account.withdraw(0)
        self.assertEqual(0, account.check_balance('1234'))







if __name__ == '__main__':
    unittest.main()
