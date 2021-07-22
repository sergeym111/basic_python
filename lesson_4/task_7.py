from functools import reduce
def my_func(n):
    for i in range(1, n + 1):
        yield i

print('Факториал = ', reduce(lambda x, y: x * y, my_func(int(input('Введите число')))))
