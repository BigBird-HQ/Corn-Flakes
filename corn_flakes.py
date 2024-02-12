# numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#
#
# def numbers_length(items):
#     count = 0
#
#     for number in items:
#         count += 1
#     return count
#
#
# print(numbers_length(numbers))
#
#
# def sum_even_positions(numbers):
#
#     sum_total = 0
#
#     for number in numbers:
#         if number % 2 == 0:
#             sum_total += number
#     return sum_total
#
#
# print(sum_even_positions(numbers))
#
#
# def sum_odd_positions(numbers):
#
#     sum_total = 0
#
#     for number in numbers:
#         if number % 2 != 0:
#             sum_total += number
#     return sum_total
#
#
# print(sum_odd_positions(numbers))
#
#
# def multiply_third_position(numbers):
#
#     product = 1
#
#     for number in numbers[2::3]:
#         product *= number
#
#     return product
#
#
# print(multiply_third_position(numbers))
#
#
# def average_of_elements(numbers):
#
#     sum_total = 0
#     average = 0
#
#     for number in numbers:
#         sum_total += number
#         average = sum_total / numbers_length(numbers)
#
#     return average
#
#
# print(average_of_elements(numbers))
#
#
# def largest_element(numbers):
#
#     largest = numbers[1]
#
#     for number in numbers:
#
#         if number > largest:
#
#             largest = number
#     return largest
#
#
# print(largest_element(numbers))
#
#
# def smallest_element(numbers):
#
#     smallest = numbers[2]
#
#     for number in numbers:
#         if number < smallest:
#             smallest = number
#     return smallest
#
#
# print(smallest_element(numbers))
#
#
# def string_list(words):
#
#     result = []
#     for word in words:
#         if len(word) >= 2 and word[0] == word[-1]:
#             result.append(word)
#             return [word]
#
#
# sample_words = ["boot", "pep", "ewe", "small", "large", "saga", "pump"]
# print(string_list(sample_words))
#
