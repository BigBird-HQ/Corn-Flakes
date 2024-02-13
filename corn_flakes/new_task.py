def sequential_list():
    new_item = []
    for number in range(1, 16):
        new_item.append(number)
    return new_item


def num():
    item = []
    for number in range(1, 16):
        item += [number]
    return item


def double_list(my_list):
    my_list2 = []

    for number in my_list:
        my_list2.append(number)
        my_list2.append(number)
    return my_list2


def remove_duplicate(mylist):
    return list(set(mylist))


#   my_list2 = []
#   for index in range(0, len(mylist), 2):
#   my_list2.append(mylist[index])
#   return my_list2


# def duplicate_number(param):
#   return [param, param]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def add_third_elements(my_list):
    sum_total = 0

    for number in range(0, len(my_list), 3):
        sum_total += number
    return sum_total


def sum_first_middle_last_elements(my_list):
    sum_total = 0
    length = len(my_list)
    sum_total += my_list[0]
    sum_total += my_list[length - 1]
    if length % 2 == 0:
        sum_total += (my_list[length // 2 - 1] + my_list[length // 2]) // 2
    else:
        sum_total += my_list[length // 2]

    return sum_total

