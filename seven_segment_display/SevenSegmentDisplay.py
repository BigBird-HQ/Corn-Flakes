from seven_segment_display.InvalidInputException import InvalidInputException


class SevenSegmentDisplay:
    def seven_segment_display(self, value):
        my_display = []
        my_display += value
        self.horizontal_display(my_display[0])
        self.vertical_display(my_display[5], my_display[1])
        self.horizontal_display(my_display[6])
        self.vertical_display(my_display[4], my_display[2])
        self.horizontal_display(my_display[3])
        self.invalid_input(value)

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
        if value != 8:
            if value != '0' and value != '1':
                raise InvalidInputException('Invalid Input!')


if __name__ == "__main__":
    segment = SevenSegmentDisplay()
    num = input('Enter binary: ')
    segment.seven_segment_display(num)
