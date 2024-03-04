import unittest

from diary_app.Diary import Diary


class MyTestCase(unittest.TestCase):
    def test_that_diary_is_unlocked_at_creation(self):
        diary = Diary('username', 'password')
        self.assertFalse(diary.is_locked())

    def test_that_diary_can_be_locked(self):
        diary = Diary('username', 'password')
        diary.is_locked()
        self.assertFalse(diary.is_locked())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_that_diary_can_be_unlocked(self):
        diary = Diary('username', 'password')
        diary.is_locked()
        self.assertFalse(diary.is_locked())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('password')
        self.assertFalse(diary.is_locked())

    def test_that_entry_can_be_created(self):
        diary = Diary('username', 'password')
        diary.is_locked()
        self.assertFalse(diary.is_locked())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('password')
        self.assertFalse(diary.is_locked())
        diary.create_entry('title', 'body')
        self.assertEqual(1, diary.get_number_of_entry())

    def test_that_more_than_one_entry_can_be_created(self):
        diary = Diary('username', 'password')
        diary.is_locked()
        self.assertFalse(diary.is_locked())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('password')
        self.assertFalse(diary.is_locked())
        diary.create_entry('title', 'body')
        diary.create_entry('title1', 'body1')
        self.assertEqual(2, diary.get_number_of_entry())

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




if __name__ == '__main__':
    unittest.main()
