seasons = [['Весна','Март','Апрель','Май'],
           ['Лето','Июнь','Июль','Август'],
           ['Осень','Сентябрь','Октябрь','Ноябрь'],
           ['Зима','Декабрь','Январь','Февраль']]
months = ['Январь', 'Февраль', 'Март',
          'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь',
          'Октябрь', 'Ноябрь', 'Декабрь']
season_dict = {'Весна':[3, 4, 5],
               'Лето':[6, 7, 8],
               'Осень':[9, 10, 11],
               'Зима':[12, 1, 2]
              }
while True:
    user_month = input('Введите номер месяца: ')
    if not user_month.isdigit():
        print('Введено не целое положительное число')
        continue
    if not (1 <= int(user_month) <= 12):
        print('Нужно число в диапазоне 1...12')
        continue
    user_month_name = months[int(user_month)-1]
# Проверка условия для списка
    for i in seasons:
        if user_month_name in i:
            print('Время года: ', i[0])
# Проверка условия для словаря
    for key in season_dict:
        if int(user_month) in season_dict[key]:
            print('Время года: ', key)