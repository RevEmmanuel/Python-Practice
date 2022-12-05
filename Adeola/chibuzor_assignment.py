def largest_of(numbers):
    return max(numbers)


def reverse_of(numbers):
    reverse_list = []
    for i in range(len(numbers) - 1, -1, -1):
        reverse_list.append(numbers[i])
    return reverse_list


def occurs_in(find, listing):
    found = False
    for values in listing:
        if find == values:
            found = True
            break
    return found


def odd_elements(listing):
    odd_list = []
    for i in range(1, len(listing), 2):
        odd_list.append(listing[i])
    return odd_list


def even_elements(listing):
    even_list = []
    for i in range(0, len(listing), 2):
        even_list.append(listing[i])
    return even_list


def running_total(listing):
    total = 0
    for value in listing:
        total += value
    return total


def is_string_palindrome(word):
    reverse_word = ''
    for i in range(len(word) - 1, -1, -1):
        reverse_word += word[i]
    return reverse_word.lower() == word.lower()


def concatenate_two_lists(list_1, list_2):
    concat_list = list_1 + list_2
    return concat_list


def combine_lists(list_1, list_2):
    combine_list = []
    length = len(list_2)
    if len(list_1) > len(list_2):
        length = len(list_1)
    for i in range(0, length):
        if len(list_1) > i:
            combine_list.append(list_1[i])
        if len(list_2) > i:
            combine_list.append(list_2[i])
    return combine_list


def digits_of(number):
    digits = []
    while number != 0:
        digits.append(number % 10)
        number //= 10
    return reverse_of(digits)


def swap(listing):
    listing[0], listing[1] = listing[1], listing[0]
    return listing


def count_numbers(strings):
    count = 0
    numbers = "0123456789"
    for letter in strings:
        if letter in numbers:
            count += 1
    return count


def odd_of(param):
    odd = 0
    for number in param:
        if number % 2 != 0:
            odd = number
            break
    return odd


def find_missing_number(param):
    for number in range(0, len(param)):
        if param[number] != param[number + 1] - 1:
            return param[number] + 1


def find_index_that_sum_to_target(param1, param2):
    for number in range(len(param1)):
        for number2 in range(number + 1, len(param1)):
            addition = param1[number] + param1[number2]
            if addition == param2:
                return [number, number2]


def is_unique(param1):
    new_list = []
    for value in param1:
        if value in new_list:
            return False
        else:
            new_list.append(value)
    return True


def sum_diagonal(param1):
    count = 0
    addition = 0
    for lists in param1:
        addition += lists[count]
        count += 1
    return addition


def first_second(param1):
    highest = param1[0]
    second_highest = param1[0]
    for number in param1:
        if number > highest:
            second_highest = highest
            highest = number
    return [highest, second_highest]


def search_insert(param1, param2):
    for i in range(len(param1)):
        if param1[i] == param2:
            return i
    else:
        for i in range(len(param1) - 1):
            if param1[len(param1) - 1] < param2:
                return len(param1)
            if param1[0] > param2:
                return 0
            if param1[i] < param2 < param1[i + 1]:
                return i + 1
