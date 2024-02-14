def swap_string(value1, value2):
    first = ''
    second = ''

    for char in value1[0:2]:
       first += char
    first += value2[2]

    for char in value2[0:2]:
        second += char
    second += value1[2]

    return first + ' ' + second

value1 = 'abc'
value2 = 'xyz'
print(swap_string(value1, value2))
