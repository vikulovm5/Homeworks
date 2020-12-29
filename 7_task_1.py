class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mtrx = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2)):
                mtrx[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mtrx]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mtrx]))


my_mtrx = Matrix([[4, 10, 0],
                  [5, 3, 42],
                  [50, 8, -2]],
                 [[5, 7, 9],
                  [95, 13, 84],
                  [0, 12, 46]])
print(my_mtrx.__add__())

