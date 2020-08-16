class Matrix:

    def __init__(self, width: int = 2, height: int = 2, fill_value=0):
        self.height = height
        self.width = width
        self.rows = [[fill_value] * width for _ in range(height)]

    def __str__(self):
        return "\n".join(" ".join(map(str, self.rows)) for self.rows in self.rows)

    def set(self, row_index: int, column_index: int, value: int):
        self.rows[row_index][column_index] = value

    def get(self, row_index, column_index):
        return self.rows[row_index][column_index]

    def __add__(self, other):
        matrix_addition = []
        for i in range(self.height):
            new_row = []
            for j in range(self.width):
                addition = self.rows[i][j] + other.rows[i][j]
                new_row.append(addition)
            matrix_addition.append(new_row)

        return matrix_addition


m1 = Matrix(2, 2, 1)
m2 = Matrix(2, 2, 2)
m3 = m1 + m2
print(m3)
