from itertools import islice, count
source_list = [1, 2, 3, 4, 5]
print(*(i for i in islice(count(int(input('Введите начальное значение'))), 10)), sep='\n')
print(*(i for i in source_list))