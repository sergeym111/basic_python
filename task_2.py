# Запрос для ввода времени в секундах
time_in_seconds = int(input('Введите время в секундах:'))
# Расчет количества часов
hours = time_in_seconds // 3600
# Расчет количества минут
minutes = (time_in_seconds - hours * 3600) // 60
# Расчет количества секунд
seconds = time_in_seconds - hours * 3600 - minutes * 60
# Вывод результата с использованием форматирования
print('Время в традиционном формате {:02d} : {:02d} : {:02d}'.format(hours, minutes, seconds))


