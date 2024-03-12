from seven_segment_display.InvalidInputException import InvalidInputException


class SevenSegmentDisplay:
    def seven_segment_display(self, value):
        my_display = []
        my_display += value
        print(my_display)
        self.invalid_input(value)
        self.horizontal_display(my_display[0])
        self.vertical_display(my_display[5], my_display[1])
        self.horizontal_display(my_display[6])
        self.vertical_display(my_display[4], my_display[2])
        self.horizontal_display(my_display[3])

    def toggle(self, numbers):
        if numbers[-1] == '1':
            return True

    def horizontal_display(self, numbers):
        if numbers == '1':
            print('* * * * * *')

    def vertical_display(self, left, right):
        if left == '1' and right == '1':
            for element in range(4):
                print('*         *')
        elif left == '0' and right == '1':
            for element in range(4):
                print('          *')
        elif left == '1' and right == '0':
            for element in range(4):
                print('*          ')

    def invalid_input(self, value):
        if len(value) != 8:
            print('Invalid input')
            # raise InvalidInputException('Invalid Input! Binary must be 8 digits')
        if value != '0' and value != '1':
            print('Invalid input')
            # raise InvalidInputException('Invalid Input!')


if __name__ == "__main__":
    segment = SevenSegmentDisplay()
    num = input('Enter a binary: ')
    segment.seven_segment_display(num)
