user_string = input('Введите несколько слов, разделенных пробелами')
user_list = user_string.split()
for i, j in enumerate(user_list, 1):
    if len(j) > 10:
        print(i, j[:11]+'...')
        continue
    print(i, j)