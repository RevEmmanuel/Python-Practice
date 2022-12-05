import math
import random
# global first_class_seat
global economy_seat


def twelve_days_of_christmas():
    for day in range(1, 12):
        dayth = {
            1: "first",
            2: "second",
            3: "third",
            4: "fourth",
            5: "fifth",
            6: "sixth",
            7: "seventh",
            8: "eighth",
            9: "ninth",
            10: "tenth",
            11: "eleventh",
            12: "twelfth"
        }
        print(f'On the {dayth[day]} day of christmas my true love said to me,', end=' ')

        gift = {
            1: "A partridge in a pear tree",
            2: "Two turtle doves,\n" +
               "And a partridge in a pear tree",
            3: "Three French hens,\n" +
               "Two turtle doves,\n" +
               "And a partridge in a pear tree.",
            4: "Four calling birds, \n" +
               "Three French hens,\n" +
               "Two turtle doves,\n" +
               "And a partridge in a pear tree.",
            5: "Five gold rings, \n" +
               "Four calling birds, \n" +
               "Three French hens,\n" +
               "Two turtle doves,\n" +
               "And a partridge in a pear tree.",
            6: "Six geese a-laying \n" +
               "Five gold rings, \n" +
               "Four calling birds, \n" +
               "Three French hens,\n" +
               "Two turtle doves,\n" +
               "And a partridge in a pear tree.",
            7: "Seven swans a-swimming \n" +
               "Six geese a-laying \n" +
               "Five gold rings, \n" +
               "Four calling birds, \n" +
               "Three French hens,\n" +
               "Two turtle doves,\n" +
               "And a partridge in a pear tree.",
            8: "Eight maids a-milking \n" +
               "Seven swans a-swimming \n" +
               "Six geese a-laying \n" +
               "Five gold rings, \n" +
               "Four calling birds, \n" +
               "Three French hens,\n" +
               "Two turtle doves,\n" +
               "And a partridge in a pear tree.",
            9: "nine ladies dancing \n" +
               "Eight maids a-milking \n" +
               "Seven swans a-swimming \n" +
               "Six geese a-laying \n" +
               "Five gold rings, \n" +
               "Four calling birds, \n" +
               "Three French hens,\n" +
               "Two turtle doves,\n" +
               "And a partridge in a pear tree.",
            10: "Ten lords a-leaping \n" +
                "nine ladies dancing \n" +
                "Eight maids a-milking \n" +
                "Seven swans a-swimming \n" +
                "Six geese a-laying \n" +
                "Five gold rings, \n" +
                "Four calling birds, \n" +
                "Three French hens,\n" +
                "Two turtle doves,\n" +
                "And a partridge in a pear tree.",
            11: "Eleven pipers piping \n" +
                "Ten lords a-leaping \n" +
                "nine ladies dancing \n" +
                "Eight maids a-milking \n" +
                "Seven swans a-swimming \n" +
                "Six geese a-laying \n" +
                "Five gold rings, \n" +
                "Four calling birds, \n" +
                "Three French hens,\n" +
                "Two turtle doves,\n" +
                "And a partridge in a pear tree.",
            12: "Twelve drummers drumming \n" +
                "Eleven pipers piping \n" +
                "Ten lords a-leaping \n" +
                "nine ladies dancing \n" +
                "Eight maids a-milking \n" +
                "Seven swans a-swimming \n" +
                "Six geese a-laying \n" +
                "Five gold rings, \n" +
                "Four calling birds, \n" +
                "Three French hens,\n" +
                "Two turtle doves,\n" +
                "And a partridge in a pear tree."
        }
        print(f'{gift[day]}')


def guess_the_number():
    random_number = random.randint(1, 1000)
    print(random_number)
    guessed_number = int(input('Enter your number: '))
    while guessed_number != random_number:
        if guessed_number > random_number:
            print('Too high')
        else:
            print('Too low')
        guessed_number = int(input('Enter your number: '))
    else:
        print('You guessed the number :)')
        yes_or_no = input('Do you want to play again: ')
        if yes_or_no.lower() == 'yes':
            guess_the_number()
        else:
            print('Thanks for playing!')


def modify_guess_the_number():
    random_number = random.randint(1, 1000)
    counter = 0
    print(random_number)
    guessed_number = int(input('Enter your number: '))
    counter += 1
    while guessed_number != random_number:
        if guessed_number > random_number:
            print('Too high')
        else:
            print('Too low')
        guessed_number = int(input('Enter your number: '))
        counter += 1
    else:
        print('You guessed the number :)')
        if counter <= 10:
            print('Aha! You know the secret!')
        else:
            print('You should be able to do better!\nWhy should it take more than 10 guesses?')
        yes_or_no = input('Do you want to play again: ')
        if yes_or_no.lower() == 'yes':
            guess_the_number()
        else:
            print('Thanks for playing!')


def hypotenuse_of(side_1, side_2):
    squares = math.pow(side_1, 2) + math.pow(side_2, 2)
    return math.sqrt(squares)


def is_multiple(num_1, num_2):
    if not num_2 % num_1:
        return True
    else:
        return False


def kelvin_of(celsius):
    return celsius + 273.15


def celsius_of(kelvin):
    return kelvin - 273.15


def pixel_quantization(pixel):
    for counter in range(len(pixel)):
        result = pixel[counter]
        if 0 <= result <= 20:
            pixel[counter] = 10
        elif 21 <= result <= 40:
            pixel[counter] = 30
        elif 21 <= result <= 40:
            pixel[counter] = 30
        elif 41 <= result <= 60:
            pixel[counter] = 50
        elif 61 <= result <= 80:
            pixel[counter] = 70
        elif 81 <= result <= 100:
            pixel[counter] = 90
        elif 101 <= result <= 120:
            pixel[counter] = 110
        elif 121 <= result <= 140:
            pixel[counter] = 130
        elif 141 <= result <= 160:
            pixel[counter] = 150
        elif 161 <= result <= 180:
            pixel[counter] = 170
        else:
            pixel[counter] = 190
    return pixel


def airline_reservation():
    first_class_seat = 0
    economy_seat = 5
    occupy = [False, False, False, False, False, False, False, False, False, False]
    seat_no = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def first_class(in_seat, seated_no):
        global first_class_seat
        first_class_seat = 0
        if economy_seat + first_class_seat < 15:
            if first_class_seat < 5:
                in_seat[first_class_seat] = True
                print(f'You have been assigned seat {seated_no[first_class_seat + 1]} in first class.');
                first_class_seat += 1
            else:
                print('First class is full! \nWould you like to be placed in Economy section? ')
                replied = int(input('Enter 1 for yes and 2 for no: '))
                if replied == 1:
                    economy(in_seat, seated_no)
                else:
                    print('Next flight leaves in 3 hours!')
        else:
            print('No more available spaces.\nNext flight leaves in 3 hours!')

    def economy(in_seat, seating_no):
        global economy_seat
        if economy_seat + first_class_seat < 15:
            if economy_seat < 10:
                in_seat[economy_seat] = True
                print(f'You have been assigned seat {seating_no[economy_seat + 1]} in economy class.')
                economy_seat += 1
            else:
                print('Economy is full! \nWould you like to be placed in FirstClass')
                reply = int(input('Enter 1 for yes and 2 for no: '))
                if reply == 1:
                    first_class(in_seat, seating_no)
                else:
                    print('Next flight leaves in 3 hours!')
        else:
            print('No more available spaces.\nNext flight leaves in 3 hours!')

    for counting in range(12):
        seat_class = int(input('Enter 1 for First class or Enter 2 for Economy: '))
        if seat_class == 1:
            first_class(occupy, seat_no)
        elif seat_class == 2:
            economy(occupy, seat_no)


def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


if __name__ == '__main__':
    twelve_days_of_christmas()
    guess_the_number()
    modify_guess_the_number()
    
    side = int(input('Enter the length of side 1: '))
    sides = int(input('Enter the length of side 2: '))
    print(f'The hypotenuse is {hypotenuse_of(side, sides)}')
    for count in range(3):
        first_num = int(input('Enter the first number: '))
        second_num = int(input('Enter the second number: '))
        if is_multiple(first_num, second_num):
            print(f'{second_num} is a multiple of {first_num}')
        else:
            print(f'{second_num} is not a multiple of {first_num}')
    side = int(input('Enter the temperature in kelvin: '))
    print(f'{side} in Celsius is {celsius_of(side) : .2f}')
    sides = int(input('Enter the temperature in celsius: '))
    print(f'{sides} in Celsius is {kelvin_of(sides)}')
    pixels = [15, 18, 22, 27, 44, 98, 183, 195, 179, 164, 148, 139, 111, 75, 86]
    print(pixel_quantization(pixels))
    # airline_reservation()
    side = int(input('Enter the digits to sum: '))
    print(f'The sum is {sum_of_digits(side)}')


def reverse_list(list_to_reverse):
    new_list = []
    for i in range(len(list_to_reverse) - 1, -1, -1):
        new_list.append(list_to_reverse[i])
    return new_list
