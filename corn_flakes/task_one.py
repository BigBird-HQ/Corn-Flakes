try:
    user_input = int(input("Enter number: "))

    sum_of_even = 0
    sum_of_odd = 0

    for number in range(1, user_input):

        if number % 2 == 0:
            sum_of_even += number
        else:
            sum_of_odd += number

    print("The sum of even numbers between 1 and the user input is: ", sum_of_even)
    print("The sum of odd numbers between 1 and the user input is: ", sum_of_odd)

except ValueError:
    print("Invalid input enter a number instead")



