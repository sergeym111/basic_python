with open('salary.txt', 'r', encoding='UTF-8') as f_salary:
    sum = 0
    count = 0
    for i in f_salary:
        if int(i.split()[1]) < 20000:
            print('Сотрудники с зарплатой, меньшей 20 000')
            print(i.split()[0])
        sum += int(i.split()[1])
        count +=1
    avg = sum / count
    print(f'Средняя зарплата {avg:.2f}')

