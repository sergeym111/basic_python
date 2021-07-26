class Storage:
    def __init__(self, name):
        self.name = name
        self.items = []

    def receipt(self, item):
        self.items.append(item)
        item.registered = self.name
        print(item.vendor, 'добавлен на склад', self.name)

    def debiting(self, item):
        item.registered = False
        print(item.vendor, 'списан со на склада', self.name)
        self.items.remove(item)


    def see_content(self):
        print(f"Товары на складе {self.name}")
        if self.items != []:
            for i in self.items:
                print(f'{i}\n')
        else:
            print(f"Склад {self.name} пуст")


class Equipment:
    def __init__(self, new):
        self.new = new
        self.registered = False

    def __str__(self, *args):
        return (f"Состояние - {'Новый' if self.new else 'Б/у'}\n"
                f"Тип {self.type}\n"
                f"Производитель {self.vendor}\n"
                f"Модель {self.model}\n"
                f"Цена {self.price}\n"
                f"Находится на складе: {self.registered if self.registered else 'не распределен'}")


class Printer(Equipment):
    def __init__(self, new, vendor, model, price):
        super().__init__(new)
        self.type = 'Принтер'
        self.vendor = vendor
        self.model = model
        self.price = price


class Scaner(Equipment):
    def __init__(self, vendor, model, price):
        super().__init__(self.new)
        self.type = 'Сканнер'
        self.vendor = vendor
        self.model = model
        self.price = price


class Xerox(Equipment):
    def __init__(self, vendor, model, price):
        super().__init__(self.new)
        self.type = 'Ксерокс'
        self.vendor = vendor
        self.model = model
        self.price = price


printer_1 = Printer(False, 'Samsung', '10001', 14100.0)

printer_2 = Printer(True, 'Brother', 'B002EF', 12500.5)

storage_1 = Storage('Главный')

storage_2 = Storage('Склад подразделения')

storage_1.receipt(printer_1)

storage_1.receipt(printer_2)

storage_1.see_content()

storage_1.debiting(printer_1)

storage_2.receipt(printer_1)

storage_1.see_content()

storage_2.see_content()

print('Просмотр определенного объекта\n', printer_1)
