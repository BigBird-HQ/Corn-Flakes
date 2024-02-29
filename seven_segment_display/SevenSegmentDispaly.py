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
        print('**********')


def vertical_display(num1, num2):
    if num1 == '1' and num1 == '1':
        for num in range(4):
            print('*        *')
    elif num1 == '0' and num2 == '1':
        for num in range(4):
            print('           *')
    elif num1 == '1' and num2 == '0':
        for num in range(4):
            print('*           ')


num1 = '1111111'
seven_segment_display(num1)
