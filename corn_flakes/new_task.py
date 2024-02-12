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

    # for index in range(0, len(mylist), 2):
    #     my_list2.append(mylist[index])
    # return my_list2


def duplicate_number(param):
    return [param, param]
