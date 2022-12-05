def my_fun(a, b):
    print(a, b)


if __name__ == '__main__':
    list_1 = ['Simi', 'Amirah', 'Seun', 'Henry', 'Adewunmi', 'Adeola', 'Simi', 'Amirah', 'Seun', 'Henry', 'Adewunmi', 'Adeola']
    new_list = [x if 'e' in x else 'Absent' for x in list_1]
    print(new_list)
    list_2 = list_1 + ['Adewunmi', 'Amala']
    print(list_2)
