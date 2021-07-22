class Stationary:
    title = 'Stationary'

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print("Рисуем ручкой")

class Pencil(Stationary):
    def draw(self):
        print("Рисуем карандашом")

class Handle(Stationary):
    def draw(self):
        print("Рисуем маркером")


my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()