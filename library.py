#===============================================================================================#
#                                           Matrizes                                            #
class matriz():
    def __init__(self, rows=3, collumns=3):
        self.matriz = []
        for i in range(0, rows, 1):
            self.matriz.append([0] * collumns)

    def __str__(self):
        rows = ""
        for row in self.matriz:
            rows = rows + str(row) + "\n"
        return rows

    def SetMatriz(self, a, b):
        if b < a or b[1] < a[1]:
            raise Exception("the first value it must be greater than the second value")

        for row in range(a[0], b[0]+1, 1):
            for collumn in range(a[1], b[1]+1, 1):
                self.matriz[row][collumn] = 1

