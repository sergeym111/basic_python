my_file = open('my_file.txt', 'w', encoding='utf-8')
while True:
    str_to_write = input('Введите строку')
    if str_to_write != '':
        my_file.write(str_to_write+'\n')
    else:
        break
my_file.close()