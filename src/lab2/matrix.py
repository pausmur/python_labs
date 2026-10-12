#Транспонирование матрицы (меняем местами строки и столбцы)
def transpose(matrix):
    if matrix == []: return []
    rows_number = len(matrix)
    columns_number = len(matrix[0])
    matrixT = []
    for row in matrix:
        if len(row) != columns_number: raise ValueError('Введена рваная матрица')
    for element1 in range(columns_number):
        row = []
        for element2 in range(rows_number):
            row.append(matrix[element2][element1])
        matrixT.append(row)
    return matrixT


print(transpose([[1,2,3]]))
print(transpose([[1],[2],[3]]))
print(transpose([[1,2],[3,4]]))
print(transpose([]))
print(transpose([[1,2],[3]]))

def row_sums(matrix):
    if matrix == []: return []
    rows_number = len(matrix)
    columns_number = len(matrix[0])
    row_summ = []
    for row in matrix:
        if len(row) != columns_number: raise ValueError('Введена рваная матрица')
        row_summ.append(sum(row))
    return row_summ

print(row_sums([[1,2,3],[4,5,6]]))
print(row_sums([[-1,1],[10,-10]]))
print(row_sums([[0,0],[0,0]]))
print(row_sums([[1,2],[3]]))

def col_sums(matrix):
    if matrix == []: return []
    rows_number = len(matrix)
    columns_number = len(matrix[0])
    row_summ = []
    for row in matrix:
        if len(row) != columns_number: raise ValueError('Введена рваная матрица')
    col_summ = [0] * columns_number
    for element1 in range(rows_number):
        for element2 in range(columns_number):
            col_summ[element2] += matrix[element1][element2]
    return col_summ

print(col_sums([[1,2,3],[4,5,6]]))
print(col_sums([[-1,1],[10,-10]]))
print(col_sums([[0,0],[0,0]]))
print(col_sums([[1,2],[3]]))

        

    