def my_func(a_1, a_2, a_3):
    if a_1 < a_2:
        if a_1 < a_3:
            return a_3 + a_2
        else:
            return a_1 + a_2
    if a_2 < a_1:
        if a_2 < a_3:
            return a_1 + a_3


while True:
    print(('Введите три разных числа'))
    a_1 = float(input('Введите 1-е число'))
    a_2 = float(input('Введите 2-е число'))
    a_3 = float(input('Введите 3-е число'))
    if a_1 == a_2 or a_2 == a_3 or a_1 == a_3:
        print('Введите различающиеся числа')
        continue
    print('сумма двух наибольших чисел из введенных', my_func(a_1, a_2, a_3))
