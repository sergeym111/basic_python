class Worker:
    def __init__(self, n, s, p, o, pr):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': o, 'bonus': pr}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname}')

    def get_total_income(self):
        print(f"Доход сотрудника: {self.name} {self.surname}: {self._income['wage']+self._income['bonus']}")


a = Position('Петр', 'Иванов', 'Рабочий', 10000, 500)

a.get_full_name()
a.get_total_income()