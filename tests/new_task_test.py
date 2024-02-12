import unittest

from corn_flakes.new_task import sequential_list, double_list, duplicate_number, remove_duplicate


class NewTaskTest(unittest.TestCase):
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def test_that_function_can_generate_numbers(self):
        actual = sequential_list()
        self.assertEqual(self.expected, actual)  # add assertion here

    def test_that_each_element_in_the_list_can_be_duplicated(self):
        expect = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
        my_list = sequential_list()
        doubled_list = double_list(my_list)
        self.assertListEqual(expect, doubled_list)

    def test_that_duplicates_in_the_list_can_be_removed(self):
        my_list = sequential_list()
        doubled_list = double_list(my_list)
        removed_duplicate = remove_duplicate(doubled_list)

        self.assertListEqual(self.expected, removed_duplicate)

    def test_that_duplicates_with_difference_in_the_list_can_be_removed(self):
        for_test = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 1,
                    15]
        removed_duplicate = remove_duplicate(for_test)

        self.assertListEqual(self.expected, removed_duplicate)





if __name__ == '__main__':
    unittest.main()
