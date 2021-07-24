class ComplexOps:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.out = f"{x} + {y} * i"

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.x * other.x - self.y * other.y} + {self.x * other.y - self.y * other.x} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


z_1 = ComplexOps(6, 7)
z_2 = ComplexOps(1, 5)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)