import unittest

from diary_app.Diary import Diary


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diary = Diary('username', 'password')

    def test_that_diary_is_unlocked_at_creation(self):

        self.assertFalse(self.diary.is_locked())

    def test_that_diary_can_be_locked(self):

        self.diary.is_locked()
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_can_be_unlocked(self):
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())

    def test_that_entry_can_be_created(self):
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())
        self.diary.create_entry('title', 'body')
        self.assertEqual(1, self.diary.get_number_of_entry())

    def test_that_more_than_one_entry_can_be_created(self):
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())
        self.diary.create_entry('title', 'body')
        self.diary.create_entry('title1', 'body1')
        self.assertEqual(2, self.diary.get_number_of_entry())

    def test_that_entry_can_be_found(self):
        diary = Diary('username', 'password')
        diary.is_locked()
        self.assertFalse(diary.is_locked())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('password')
        self.assertFalse(diary.is_locked())
        diary.create_entry('title', 'body')
        diary.create_entry('title1', 'body1')
        found_entry = diary.find_entry_by_id(2)
        self.assertEqual(diary.find_entry_by_id(2), found_entry)

    def test_that_entry_can_be_deleted(self):

        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())
        self.diary.create_entry('title', 'body')
        self.diary.create_entry('title1', 'body1')
        self.diary.delete_entry(2)
        self.assertEqual(1, self.diary.get_number_of_entry())

    def test_that_entry_can_be_updated(self):
        self.diary.is_locked()
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())
        self.diary.create_entry('title', 'body')
        self.diary.create_entry('title1', 'body1')
        self.diary.update_entry(2, 'updated_title', 'updated_body')
        found = self.diary.find_entry_by_id(2)
        self.assertEqual("updated_body", found.get_body())


if __name__ == '__main__':
    unittest.main()
