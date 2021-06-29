goods = [(1,{'Марка':'BMW', 'Цена':5400000.00, 'Количество':2}),
         (2,{'Марка':'Renault', 'Цена':1450000.00, 'Количество':11}),
         (3,{'Марка':'Audi', 'Цена':3480000.00, 'Количество':5})
         ]
new_keys = list(goods[0][1].keys()) # получение списка ключей целевого словаря
lists = [] # пустой список для списка списков значений из исходных словарей
# lists = [0] * len(new_keys)
list_to_stat = [] # список для группировки значений в целевую таблицу
for num, val in enumerate(goods):
    lists.append(list(val[1].values())) # извлечение списка значений из исходного словаря
for i in range(len(new_keys)): # транспонирование списка значений
    row = []
    for j in range(len(goods[0][1])):
        row.append(lists[j][i])
    list_to_stat.append(row)
stat = {} # пустой целевой словарь
for num, key in enumerate(new_keys): # заполнение целевого словаря
    stat.update({new_keys[num]: list_to_stat[num]})
print(stat)