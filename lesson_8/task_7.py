class ComplexOps:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.out = f"{x} + {y} * i"

    def __add__(self, other):
        print(f'Сумма равна')
        return f'= {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'= {self.x * other.x - self.y * other.y} + {self.x * other.y - self.y * other.x} * i'

    def __str__(self):
        return f'= {self.x} + {self.y} * i'


c_1 = ComplexOps(6, 7)
c_2 = ComplexOps(1, 5)
print('c_1', c_1)
print('c_2', c_2)
print('c_1 + c_2', c_1 + c_2)
print('c_1 * c_2', c_1 * c_2)