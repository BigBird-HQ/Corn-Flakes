import unittest

from Account.InsufficientFundsError import InsufficientFundsError
from Account.InvalidAmountError import InvalidAmountError
from Account.InvalidPinError import InvalidPinError
from Account.account import Account


class MyTestCase(unittest.TestCase):
    def test_that_account_is_empty_at_creation(self):
        account = Account('Mavericks', '1234', 1)
        self.assertEqual(0, account.check_balance('1234'))

    def test_that_account_balance_can_be_checked(self):
        account = Account('Mavericks', '1234', 1)
        self.assertEqual(0, account.check_balance('1234'))

    def test_that_balance_remains_unchanged_when_zero_amount_is_deposited(self):
        account = Account('Mavericks', '1234', 1)
        with self.assertRaises(InvalidAmountError):
            account.deposit(0)
        self.assertEqual(0, account.check_balance('1234'))

    def test_that_balance_increases_when_positive_amount_is_deposited(self):
        account = Account('Mavericks', '1234', 1)
        account.deposit(2000)
        self.assertEqual(2000, account.check_balance('1234'))

    def test_that_balance_increases_when_positive_amount_is_deposited_twice(self):
        account = Account('Mavericks', '1234', 1)
        account.deposit(2000)
        account.deposit(3000)
        self.assertEqual(5000, account.check_balance('1234'))

    def test_that_negative_amount_cannot_be_withdrawn_throw_invalid_amount_exception(self):
        account = Account('Mavericks', '1234', 1)
        self.assertEqual(0, account.check_balance('1234'))
        with self.assertRaises(InvalidAmountError):
            account.deposit(-2000)
        self.assertEqual(0, account.check_balance('1234'))

    def test_that_balance_decreases_when_positive_amount_is_withdrawn(self):
        account = Account('Mavericks', '1234', 1)
        account.deposit(5000)
        account.withdraw(3000, '1234')
        self.assertEqual(2000, account.check_balance('1234'))

    def test_that_when_zero_amount_is_withdrawn_it_throws_invalid_amount_error(self):
        account = Account('Mavericks', '1234', 1)
        with self.assertRaises(InvalidAmountError):
            account.withdraw(0, '1234')
        self.assertEqual(0, account.check_balance('1234'))

    def test_that_withdrawal_amount_cannot_be_greater_than_balance_throw_insufficient_funds_exception(self):
        account = Account('Mavericks', '1234', 1)
        account.deposit(2000)
        self.assertEqual(2000, account.check_balance('1234'))
        with self.assertRaises(InsufficientFundsError):
            account.withdraw(3000, '1234')
        self.assertEqual(2000, account.check_balance('1234'))

    def test_that_wrong_pin_does_not_allow_Withdrawal_throws_invalid_pin_error(self):
        account = Account('Mavericks', '1234', 1)
        account.deposit(2000)
        self.assertEqual(2000, account.check_balance('1234'))
        with self.assertRaises(InvalidPinError):
            account.withdraw(2000, '1233')
        self.assertEqual(2000, account.check_balance('1233'))


if __name__ == '__main__':
    unittest.main()
