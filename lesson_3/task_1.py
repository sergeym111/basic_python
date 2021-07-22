def quotient(x, y):
    try:
        return (x / y)
    except (ZeroDivisionError, ValueError) as err:
        return str(err)

while True:
    num_1 = float(input('Введите первое число'))
    num_2 = float(input('Введите второе число'))
    if quotient(num_1, num_2) == 'float division by zero':
        print('Ошибка! Деление на ноль!')
        continue
    else:
        print('Результат', quotient(num_1, num_2))
