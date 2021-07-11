# Запрос значения величины выручки у пользователя
proceeds = float(input('Введите выручку: '))
# Запрос значения величины издержек
costs = float(input('Введите издержки: '))
# Определяем финансовый результат
if proceeds > costs:
    print('Фирма работает с прибылью')
    profit = proceeds - costs
    print('Рентабельнось выручки: ', profit / proceeds )
    personal = int(input('Введите количество сотрудников: '))
    print('Прибыль на одного сотрудника:', profit / personal)
else:
    print("Фирма работает в убыток")
