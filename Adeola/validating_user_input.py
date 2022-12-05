if __name__ == '__main__':
    counter, counter_1, counter_2 = 1, 0, 0
    while counter <= 10:
        try:
            result = int(input('Enter 1 for pass and 2 for fail: '))
            if result == 1 or result == 2:
                if result == 1:
                    counter_1 += 1
                else:
                    counter_2 += 1
                counter += 1
            else:
                print('Enter a valid value!')
        except ValueError:
            print('Invalid type literal entered.')
    print(f'{counter_1} students passed and {counter_2} students failed.')
    print(f'Passed : {counter_1}\nFailed : {counter_2}')
    if counter_1 > 8:
        print('Bonus to instructor!')

    print("Enter two numbers and I will tell you the comparison operators they support.")

    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if num1 > num2:
        print(num1, "is greater than", num2)
    else:
        print(num1, "is less than", num2)
    if num1 == num2:
        print(num1, "is equal to", num2)
    else:
        print(num1, "is not equal to", num2)
    if num1 >= num2:
        print(num1, "is greater than or equal to", num2)
    else:
        print(num1, "is less than or equal to", num2)
