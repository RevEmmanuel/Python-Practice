def number_1():
    new_dict = {}
    num = int(input('Enter the length of dictionary: '))
    for n in range(1, num + 1):
        new_dict[n] = n * n
    print(new_dict)


def number_2():
    count = 0
    new_set = set()
    while count < 5:
        try:
            entered_num = int(input(f'Enter number {count + 1}: '))
            if 2 <= entered_num <= 90:
                new_set.add(entered_num)
                count += 1
            else:
                print('Invalid input, try again')
        except ValueError:
            print('Please enter a valid number')
    else:
        print(new_set)


def number_3():
    new_dict = {}
    value_list = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
    key_list = [10, 20, 30, 40,  50, 60, 70, 80, 90, 100]
    indexing = 0
    for item in key_list:
        new_dict[item] = value_list[indexing]
        indexing += 1
    print(new_dict)


if __name__ == '__main__':
    number_1()
    number_2()
    number_3()
