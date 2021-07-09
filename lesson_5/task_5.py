from random import randint


with open('number_row.txt', 'w', encoding='UTF-8') as f_numbers:
    for i in range(1, 10):
        f_numbers.write(str(randint(1, 100)) + ' ')

with open('number_row.txt', 'r', encoding='UTF-8') as f_numbers:
    my_list = [int(i) for i in f_numbers.read().split()]
    print(f'Сумма чисел в файле {sum(my_list)}')
