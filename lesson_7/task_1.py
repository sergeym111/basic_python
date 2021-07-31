class Matrix:
    def __init__(self, input_matrix):
        self.matrix = input_matrix
        if type(self.matrix) != list:
            print('Исходные данные - не матрица')

    def __str__(self):
        out = ''
        for i in self.matrix:
            for j in i:
                out += f"{j} "
            out += '\n'
        return out

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                temp = self.matrix[i][j] + other.matrix[i][j]
                result[i].append(temp)
        return result


input_matrix = [[12, 14],
                [16, 17],
                [22, 33],
                [27, 49]]
input_matrix_1 = [[1, 1],
                  [1, 1],
                  [1, 1],
                  [1, 1]]
matrix_1 = Matrix(input_matrix)
matrix_2 = Matrix(input_matrix_1)
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
