import unittest

from corn_flakes import new_task_three


class NewTaskThreeTest(unittest.TestCase):
    expected = 'xyc abz'

    def test_that_function_can_swap_to_single_string_from_double_string(self):
        value1 = 'abc'
        value2 = 'xyz'
        expected = 'abz xyc'
        self.assertEqual('abz xyc', new_task_three.swap_string(value1, value2))





if __name__ == '__main__':
    unittest.main()
