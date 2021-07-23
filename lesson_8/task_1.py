class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def date_transform(cls, self):
        return [int(i) for i in self.split('-')]

    @staticmethod
    def date_check(date):
        year = month = day = False
        if date[2] <= 2021:
            year = True
        if date[1] in [i for i in range(1, 13)]:
            month = True
        if date[0] in [i for i in range(1, 31)]:
            day = True
        if day and month and year:
            return f'Дата проверена, все ОК!'
        else:
            return f'Дата не прошла проверку'

    def __str__(self):
        return f'Заданная дата {Data.date_transform(self.date)[0]}-' \
               f'{Data.date_transform(self.date)[1]}-' \
               f'{Data.date_transform(self.date)[2]}'


day = Data('11-12-2021')
print(day)
print(day.date_check(day.date_transform(day.date)))
day_2 = Data('12-22-2031')
print(day_2)
print(day.date_check(day.date_transform(day_2.date)))
