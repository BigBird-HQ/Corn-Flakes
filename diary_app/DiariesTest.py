import unittest

from diary_app.Diaries import Diaries


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_that_diary_can_be_added_to_diaries(self):
        self.diaries.add('username', 'password')
        self.assertEqual(1, self.diaries.get_number_of_diaries())

    def test_that_more_diary_can_be_added_to_diaries(self):
        self.diaries.add('username', 'password')
        self.diaries.add('username1', 'password')
        self.assertEqual(2, self.diaries.get_number_of_diaries())

    def test_that_diary_found_by_username(self):
        self.diaries.add('username', 'password')
        self.diaries.add('username1', 'password')
        expected = self.diaries.find_by_username('username1')
        self.assertEqual(expected.get_username(), 'username1')

    def test_that_diary_in_diaries_can_be_deleted(self):
        self.diaries.add('username', 'password')
        self.diaries.add('username1', 'password')
        self.diaries.find_by_username('username1')
        self.diaries.delete('username', 'password')
        self.assertEqual(1, self.diaries.get_number_of_diaries())


if __name__ == '__main__':
    unittest.main()
