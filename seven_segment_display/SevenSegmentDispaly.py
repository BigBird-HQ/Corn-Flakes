def seven_segment_display(value):
    my_display = []
    my_display += value
    horizontal_display(my_display[0])
    vertical_display(my_display[5], my_display[1])
    horizontal_display(my_display[6])
    vertical_display(my_display[4], my_display[2])
    horizontal_display(my_display[3])


def horizontal_display(num):
    if num == '1':
        print('* * * * * *')


def vertical_display(left, right):
    if left == '1' and right == '1':
        for number in range(4):
            print('*         *')
    elif left == '0' and right == '1':
        for number in range(4):
            print('          *')
    elif left == '1' and right == '0':
        for number in range(4):
            print('*          ')


if __name__ == "__main__":
    num = input('Enter binary: ')
    seven_segment_display(num)
