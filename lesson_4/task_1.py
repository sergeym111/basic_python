from sys import argv

name, vyr, st, pr = argv
zp = float(vyr) * float(st) + float(pr)
print(f'Выработка сотрудника {vyr}, ставка {st}, премия {pr}, зарплата {zp}')

