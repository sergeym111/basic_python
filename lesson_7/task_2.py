from abc import ABC, abstractmethod
class Clothes:
    intake = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def info(self):
        pass

    def show_intake(self):
        print('Всего потрачено ткани :', Clothes.intake)


class Cout(Clothes):

    def __init__(self, name, size):
        self.type = 'cout'
        self.name = name
        self.size = size
        Clothes.intake += self.size / 6.5 + 0.5

    def info(self):
        print('Вид одежды: ', self.type)
        print('Название модели :', self.name)
        print('Размер: ', self.size)
        print('Расход ткани: ', self.size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, name, height):
        self.type = 'suit'
        self.name = name
        self.height = height
        Clothes.intake += self.height * 2 + 0.3

    def info(self):
        print('Вид одежды: ', self.type)
        print('Название модели :', self.name)
        print('Рост: ', self.height)
        print('Расход ткани: ', self.height * 2 + 0.3)


a = Cout('Пальто', 38)
a.info()
a.show_intake()
b = Cout('Коричневое пальто', 44)
b.info()
b.show_intake()
c = Suit('Деловой', 1.86)
c.info()
c.show_intake()
