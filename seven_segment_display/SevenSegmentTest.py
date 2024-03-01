import unittest

from seven_segment_display.InvalidInputException import InvalidInputException
from seven_segment_display.SevenSegmentDisplay import SevenSegmentDisplay


class MyTestCase(unittest.TestCase):
    def test_that_segment_display_can_be_toggled_on_or_off(self):
        segment = SevenSegmentDisplay()
        numbers = '01100001'
        self.assertTrue(segment.toggle(numbers))

    def test_that_only_zeros_and_ones_are_valid_in_segment(self):
        segment = SevenSegmentDisplay()
        numbers = '11100001'
        with self.assertRaises(InvalidInputException):
            segment.invalid_input(numbers)

    def test_that_segment_can_have_no_more_than_eight_binary_numbers(self):
        segment = SevenSegmentDisplay()
        numbers = '111111111'
        with self.assertRaises(InvalidInputException):
            segment.invalid_input(numbers)

    def test_that_segment_can_no_less_than_eight_binary_numbers(self):
        segment = SevenSegmentDisplay()
        numbers = '11111'
        with self.assertRaises(InvalidInputException):
            segment.invalid_input(numbers)




if __name__ == '__main__':
    unittest.main()
