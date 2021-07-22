class Cell:
    cell_number = 0

    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells
        Cell.cell_number += 1

    def __str__(self):
        return (f"Клетка #{Cell.cell_number} состоит из {self.number_of_cells} ячеек")

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            print('Невозможно произвести вычетание, уменьшаемое меньше, чем вычитаемое')

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def make_order(self, row_len):
        a = ''
        rows = self.number_of_cells // row_len
        reminder = self.number_of_cells % row_len
        for i in range(rows):
            a += '*' * row_len + '\n'
        a += '*' * reminder
        return a


a = Cell(12)
print(a)
b = Cell(6)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print((a + b).make_order(5))
