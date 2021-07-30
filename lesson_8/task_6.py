class Storage:
    def __init__(self, name):
        self.name = name
        self.items = []

    def receipt(self, item):
        if not item.registered:
            self.items.append(item)
        else:
            return f'Данная единица уже на складе'
        item.registered = self.name
        return f"{item.vendor} добавлен на склад {self.name}"

    def debiting(self, item):
        if item.registered:
            item.registered = False
            self.items.remove(item)
            return f"Объект списан со склада {self.name}"
        else:
            return f"{item.vendor} уже имеет статус 'не распределен'"


    def see_content(self):
        print(f"Товары на складе {self.name}")
        if self.items != []:
            for i, j in enumerate(self.items):
                print(f'{i+1}. {j}   ')
            print('\n')
        else:
            print(f"Склад {self.name} пуст")


class Equipment:
    def __init__(self, registered=False, new='Новый'):
        self.registered = registered
        self.new = new

    def __str__(self, *args):
        return (f"Тип: {self.type}  "
                f"Производитель: {self.vendor}  "
                f"Модель: {self.model}  "
                f"Состояние: {'Новый' if self.new else 'Б/у'}  "
                f"Цена: {self.price}  "           
                f"Находится на складе: {self.registered if self.registered else 'не распределен'}")

    @classmethod
    def create_obj(cls, data):
        s, m, p, n = data
        r = False
        return cls(s, m, p, n, r)


class Printer(Equipment):
    def __init__(self, vendor, model, price, new, registered):
        self.new = new
        self.vendor = vendor
        self.model = model
        try:
            self.price = float(price)
        except:
            print(f'Цена должна быть задана действительным числом')
        self.type = 'Принтер'
        super().__init__(registered)


class Scaner(Equipment):
    def __init__(self, vendor, model, price, new, registered):
        self.new = new
        self.vendor = vendor
        self.model = model
        try:
            self.price = float(price)
        except:
            print(f'Цена должна быть задана действительным числом')
        self.type = 'Сканер'
        super().__init__(registered)


class Xerox(Equipment):
    def __init__(self, vendor, model, price, new, registered):
        self.new = new
        self.vendor = vendor
        self.model = model
        try:
            self.price = float(price)
        except:
            print(f'Цена должна быть задана действительным числом')
        self.type = 'Ксерокс'
        super().__init__(registered)


def check_input(a):
    while True:
        choice = input('Введите номер пункта меню и нажмите Enter: ')
        try:
            choice = int(choice)
            if choice in a:
                return choice
                break
            else:
                print('Выберите только существующие пункты меню')
        except:
            print('Введенное значение должно быть целым числом')
            continue


def show_menu():
    print('1. Оформить новую единицу оргтехники')
    print('2. Посмотреть содержимое склада')
    print('3. Передать технику')
    print('4. Выход')
    return check_input([1, 2, 3, 4])


def show_menu_2():
    print('1. Посмотреть список складов')
    print('2. Посмотреть содержимое склада')
    print('3. Выход из меню')
    return check_input([1, 2, 3])


def show_menu_3():
    print('1. Посмотреть список техники')
    print('2. Перемещение техники')
    print('3. Выход из меню')
    return check_input([1, 2, 3])

def show_menu_4():
    print('1. Передать технику на склад')
    print('2. Списать технику со склада')
    return check_input([1, 2])


def data_prepare():
    features = []
    print('Оформляем новую единицу техники')
    features.append(input('Производитель: '))
    while True:
        a = input('Вид техники (принтер, ксерокс, сканер): ')
        if a in ['принтер', 'ксерокс', 'сканер']:
            features.append(a)
            break
        else:
            print('Техника других видов не принимается к учету')
    features.append(input('Модель: '))
    while True:
        a = input('Цена: ')
        try:
            a = float(a)
            features.append(a)
            break
        except:
            print('Введенное значение должно быть действительным числом')
    while True:
        a = input('Состояние техники (новый, б/у): ')
        if a in ['новый', 'б/у']:
            features.append(a)
            break
        else:
            print('Техника других состояний не принимается к учету')
    return features


storage = []
storage.append(Storage('Главный склад'))
storage.append(Storage('Склад подразделения'))
items = []
items.append(Printer('Samsung', '10001', 13000, 'б/у', False))
items.append(Xerox('Xerox', 'x01', 12500, 'новый', False))
items.append(Scaner('MusTech', 'BearPow', 5600, 'новый', False))
while True:
    menu_item = show_menu()
    if menu_item == 1:
        obj_data = data_prepare()
        print(obj_data)
        if obj_data[1] == 'принтер':
            items.append(Printer.create_obj([obj_data[0], obj_data[2], obj_data[3], obj_data[4]]))
        if obj_data[1] == 'ксерокс':
            items.append(Xerox.create_obj([obj_data[0], obj_data[2], obj_data[3], obj_data[4]]))
        if obj_data[1] == 'сканер':
            items.append(Scaner.create_obj([obj_data[0], obj_data[2], obj_data[3], obj_data[4]]))
    elif menu_item == 2:
        while True:
            menu_item_1 = show_menu_2()
            if menu_item_1 == 1:
                for i, j in enumerate(storage):
                    print(f'{i+1}. {j.name}')
                print('-------------------------')
            elif menu_item_1 == 2:
                num = int(input ('Введите номер склада: '))
                try:
                    storage[num-1].see_content()
                except:
                    print('Введите корректный номер склада!!!')
            elif menu_item_1 == 3:
                break
    elif menu_item == 3:
        while True:
            menu_item_2 = show_menu_3()
            if menu_item_2 == 1:
                for i, j in enumerate(items):
                    print(f'{i+1}. {j}')
            elif menu_item_2 == 2:
                while True:
                    menu_item_4 = show_menu_4()
                    if menu_item_4 == 1:
                        storage_num = int(input('Введите номер склада: '))
                        equipment_num = int(input('Введите номер техники: '))
                        print(storage[storage_num-1].receipt(items[equipment_num-1]))
                    elif menu_item_4 == 2:
                        storage_num = int(input('Введите номер склада: '))
                        equipment_num = int(input('Введите номер техники: '))
                        print(storage[storage_num - 1].debiting(items[equipment_num - 1]))
                    break
            elif menu_item_2 == 3:
                break
    elif menu_item == 4:
        print(f'Работа программы завершена')
        break
