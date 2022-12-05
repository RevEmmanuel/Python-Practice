import random
"""Comparing integers using if statements and comparison operators."""

"""
def test_student_grade(tested):
    reply = 'Null'
    if tested < 0 or tested > 100:
        reply = 'Enter a valid number!'
    else:
        if 90 <= tested <= 100:
            reply = 'A'
        elif 70 <= tested <= 89:
            reply = 'B'
        elif 50 <= tested <= 69:
            reply = 'C'
        elif 40 <= tested <= 49:
            reply = 'D'
        elif 30 <= tested <= 39:
            reply = 'E'
        elif tested < 30:
            reply = 'F\nZero Talent!'
    return reply


if __name__ == '__main__':
    # from decimal import Decimal
    # import statistics
    # import random

    print("Enter two numbers and I will tell you the comparison operators they support.")

    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if num1 > num2:
        print(num1, "is greater than", num2)
    if num1 < num2:
        print(num1, "is less than", num2)
    if num1 == num2:
        print(num1, "is equal to", num2)
    if num1 != num2:
        print(num1, "is not equal to", num2)
    if num1 >= num2:
        print(num1, "is greater than or equal to", num2)
    if num1 <= num2:
        print(num1, "is less than or equal to", num2)

     Finding the maximum and minimum of three values 
    print("Enter three numbers and I will tell you the maximum and minimum.")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3

    minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3
    
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)
    # min and max can receive any number of arguments.
    print("The minimum number is", minimum)
    print("The maximum number is", maximum)
    print("Range:", minimum, "-", maximum)
    print('Range:', min(47, 95, 88, 73, 88, 84), '-', max(47, 95, 88, 73, 88, 84))

    total = 0
    for number in [10, 20, 30, 40, -5, -8]:
        total += number
    print('The total is', total)
    for number in range(10):
        #total += number
        print(number + 1, end=' ')
        
    
    number, total, gradeCounter = 1, 0, 0
    grade = int(input('Enter the grade or -1 to end: '))
    while grade != -1 or number <= 10:
        gradeCounter += 1
        total += grade
        number += 1
        grade = int(input('Enter the grade or -1 to end: '))
    if gradeCounter != 0:
        print(f'The average of the {gradeCounter} grades is {(total / 10) : .2f}')
    else:
        print('No grades were entered.')



    grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
    gradeCounter = 0
    new_total = 0
    for grade in grades:
        new_total += grade
        gradeCounter += 1
    average = new_total / gradeCounter
    print(f'The total of the {gradeCounter} grades is {average}')
    # result = f'The total of the {gradeCounter} grades is {average}'
    # print(result)
    # print('The total of the', gradeCounter, 'grades is', new_total / gradeCounter)
    
    counter_1, counter_2 = 0, 0
    for count in range(1, 11, 1):
        # start from 1 up to but not including 11 and increase by 1
        result = int(input('Enter 1 for pass and 2 for fail: '))
        if result == 1 or result == 2:
            if result == 1:
                counter_1 += 1
            else:
                counter_2 += 1
        else:
            print('Enter a valid value!')
        # counter += 1
    print(f'{counter_1} students passed and {counter_2} students failed.')
    print(f'Passed         Failed\n     {counter_1}              {counter_2}')
    print('Passed:', counter_1)
    print('Failed:', counter_2)
    if counter_1 > 8:
        print('Bonus to instructor!')
        

    amount = Decimal('112.310')
    print(type(amount))
    # print(f'{amount : .20f}')

    a, p, r = 0, 1000, Decimal('0.05')
    print(f'Years      Amount')
    for years in range(1, 11):
        a = p * ((1 + r) ** years)
        print(f'{years : > 5}{a : > 12.2f}')
    

    grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
    print(f'The average of the {len(grades)} numbers is {sum(grades) / len(grades)}')
    print(f'The mean of the numbers is {statistics.mean(grades)}.\nThe median is {statistics.median(grades)}.\nThe '
          f'mode is {statistics.mode(grades)}')
    print(sorted(grades))
   

    for number in range(3):
        for square in range(3):
            print('0', end='')
        print()
     

    for row in range(10):
        for column in range(10):
            print('<' if row % 2 == 1 else '>', end='')
        print()
        

    x = 0
    while x < 10:
        print(x, end=' ')
        x += 1

    print(f'\nFinal value of x is {x}')

    def is_perfect_number(num):
        total = 0
        print('The factors are:', end=' ')
        for divider in range(1, num):
            if num % divider == 0:
                total += divider
                print(divider, end=' ')
        print('\nThe sum of the factors is:', total)
        return num == total

    number = int(input('Enter the number: '))
    if is_perfect_number(number):
        print(f'{number} is a perfect number!')
    else:
        print(f'{number} is not a perfect number.\nZero talent!')
        

    frequency1, frequency2, frequency3, frequency4, frequency5, frequency6 = 0, 0, 0, 0, 0, 0
    for number in range(6_000_000):
        result = random.randrange(1, 7)
        if result == 1:
            frequency1 += 1
        elif result == 2:
            frequency2 += 1
        elif result == 3:
            frequency3 += 1
        elif result == 4:
            frequency4 += 1
        elif result == 5:
            frequency5 += 1
        elif result == 6:
            frequency6 += 1

    print('Frequency     Appearance')
    print(f'{1 : > 9}     {frequency1 : > 10}')
    print(f'{2 : > 9}     {frequency2 : > 10}')
    print(f'{3 : > 9}     {frequency3 : > 10}')
    print(f'{4 : > 9}     {frequency4 : > 10}')
    print(f'{5 : > 9}     {frequency5 : > 10}')
    print(f'{6 : > 9}     {frequency6 : > 10}')
    frequency = [frequency1, frequency2, frequency3, frequency4, frequency5, frequency6]
    print(sum(frequency))
    

    frequency1, frequency2, frequency3, frequency4, frequency5, frequency6 = 0, 0, 0, 0, 0, 0
    random.seed(32)
    for number in range(10):
        result = random.randrange(1, 7)
        print(result, end=' ')
        if result == 1:
            frequency1 += 1
        elif result == 2:
            frequency2 += 1
        elif result == 3:
            frequency3 += 1
        elif result == 4:
            frequency4 += 1
        elif result == 5:
            frequency5 += 1
        elif result == 6:
            frequency6 += 1
    print('\nFrequency     Appearance')
    print(f'{1 : > 9}     {frequency1 : > 10}')
    print(f'{2 : > 9}     {frequency2 : > 10}')
    print(f'{3 : > 9}     {frequency3 : > 10}')
    print(f'{4 : > 9}     {frequency4 : > 10}')
    print(f'{5 : > 9}     {frequency5 : > 10}')
    print(f'{6 : > 9}     {frequency6 : > 10}')

    def average(*args):
        return sum(args) / len(args)

    grades = {12, 13, 14, 15}
    print(average(*grades))
    

    x = 15


    def local(num):
        num += 2
        print('local x is', num)

    print('global x is', x)

    count = 1
    counter = 0
    grade_acceptable = ['A', 'B', 'C', 'C', 'D', 'E', 'F']
    while count <= 5:
        result = int(input('Enter a grade: '))
        response = test_student_grade(result)
        if response in grade_acceptable:
            print(f'Grade is {response}')
            count += 1
        else:
            print(response)
            counter += 1
        if counter == 3:
            print('Too many invalid values entered.')
            break
            """

'''
class FirstClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    print(random.randrange(1, 100))
'''

# random.seed(104)

number = random.randint(1, 10)
guess = int(input('Guess a number between 1 and 10: '))
count = 1
while count < 3:
    if guess == number:
        print('You guessed right :)')
        break
    else:
        print('Try again.:(')
        guess = int(input('Guess a number between 1 and 10: '))
    count = count + 1
else:
    print(f'No more guesses.\nThe correct guess is {number}. Better luck next time, OLODO!')
