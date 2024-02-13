my_set = set()

count = 0

while count < 10:
    user = int(input("Enter ten numbers: "))
    my_set.add(user)
    count += 1


def sum_collection(my_set):
    sum_total = 0

    for number in my_set:
        sum_total += number

    return sum_total


def remove_item(my_set, number):

    for element in my_set:
        if