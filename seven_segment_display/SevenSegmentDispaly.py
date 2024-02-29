def seven_segment_display(value):
    my_display = []
    my_display += value


def horizontal_display(num):
    if num == '1':
        print('*******')


def vertical_display(num1, num2):
    if num1 == '1' and num1 == '1':
        for num in range(4):
            print('*        *')
    elif num1 == '0' and num2:
        for num in range(4):
            print('           *')
    elif num1 == '1' and num2 == '0':
        for num in range(4):
            print('*           ')


num1 = ''
seven_segment_display(num1)
