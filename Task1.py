class Matrix:
    result_matrix = []

    def __init__(self, input_matrix):
        self.output_matrix = '\n'.join(['\t'.join([str(column) for column in row]) for row in input_matrix])
        self.input_matrix = [[column for column in row] for row in input_matrix]

    def __str__(self):
        return str(self.output_matrix)

    def __add__(self, other):
        for row in range(len(self.input_matrix)):
            for column in range(len(other.input_matrix[0])):
                self.input_matrix[row][column] = self.input_matrix[row][column] + other.input_matrix[row][column]
            self.result_matrix = self.input_matrix
        return Matrix(self.result_matrix)


m1 = Matrix([[11, 0, 11, 0, 11], [0, 11, 0, 11, 0], [11, 0, 11, 0, 11], [0, 11, 0, 11, 0], [11, 0, 11, 0, 11]])
m2 = Matrix([[0, 22, 0, 22, 0], [22, 0, 22, 0, 22], [0, 22, 0, 22, 0], [22, 0, 22, 0, 22], [0, 22, 0, 22, 0]])
print(m1)
print()
print(m2)
print()
print(m1 + m2)
print()
print(m1 + m2)