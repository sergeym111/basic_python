my_list = [1, 2.6, 2 + 1j, True, 'zed']
for i in enumerate(my_list):
    print('Тип {}-го элемента {}'.format(i[0], type(i[1])))
