number_of_elements = int(input('Введите длину списка: '))
my_list = [0] * number_of_elements
for i in enumerate(my_list):
    my_list[i[0]] = input('Введите {}-й элемент списка: '.format(i[0]))
print('Заданный список: ', my_list)
for i in enumerate(my_list, 1):
    if i[0] % 2 != 0 and i[0] != number_of_elements:
        my_list[i[0]-1], my_list[i[0]] = my_list[i[0]], my_list[i[0]-1]
    elif i[0] % 2 != 0 and i[0] == number_of_elements:
        print('В списке нечетное количество элементов, последний элемент не изменён')
print('Список с перестановкой: ', my_list)
