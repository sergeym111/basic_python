with open('my_file_2.txt', 'a', encoding='UTF-8') as my_file:
    my_file.writelines(['Артем 3343 2323 муж\n',
                        'Марина 2323 12 жен\n',
                        'Пересвет 12 232 муж\n'])
with open('my_file_2.txt', 'r', encoding='UTF-8') as my_file:
    a = my_file.readlines()
    print(f'Строк в файле: {len(a)} шт.')
    for i, val in enumerate(a):
        print(f'В {i}-й строке {len(val)} символов')

