a = int(input('Введите результат в 1-й день в км: '))
b = int(input('Введите цель тренировок в км: '))
day = 0
while a <= b:
    day += 1
    print('На {} день результат {} км'.format(day, a))
    a += 0.1 * a
print('На {} день результат стал не менее {} км'.format(day + 1, b))