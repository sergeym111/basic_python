class Storage:
    def __init__(self, name):
        self.name = name


class Equipment:
    def __init__(self, new):
        self.new = True

    def __str__(self):
        return (f"Состояние - {'Новый' if self.new else 'Б/у'}")


class Printer(Equipment):
    def __init__(self, type, vendor, model, price):
        super().__init__(self.new)
        self.type = 'Принтер'
        self.vendor = vendor
        self.model = model
        self.price = price


class Scaner(Equipment):
    def __init__(self, type, vendor, model, price):
        super().__init__(self.new)
        self.type = 'Сканнер'
        self.vendor = vendor
        self.model = model
        self.price = price


class Xerox(Equipment):
    def __init__(self, type, vendor, model, price):
        super().__init__(self.new)
        self.type = 'Ксерокс'
        self.vendor = vendor
        self.model = model
        self.price = price
