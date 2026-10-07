# Лабораторная 2
## Задание A
### Функция №1 - поиск минимума и максимума в списке без использования встроенных функций min() и max()
```python
def min_max(array):
    if len(array) == 0:
        raise ValueError('Список пуст')
    else:
        array_sort = sorted(array)
        minimum = array_sort[0]
        maximum = array_sort[-1]
    return (minimum, maximum)

print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))
```
![](./images/lab02/arrays.min_max.png)

### Функция №2 - сортировка списка уникальных значений без встроенных функций sort() и sorted()
```python
def unique_sorted(array):
    unique_array = list(set(array))
    import random
    def qSort(array):
        if len(array) <= 1: return array
        random_element = random.choice(array)
        lower_random = [x for x in array if x < random_element]
        equal_random = [x for x in array if x == random_element]
        higher_random = [x for x in array if x > random_element]
        return qSort(lower_random) + equal_random + qSort(higher_random)
    sorted_array = qSort(unique_array)
    return sorted_array

print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
```
![](./images/lab02/arrays.unique_sorted.png)

### Функция №3 - расплющивание списка кортежей(матрицы) с учетом значений внутри (не числа не принимаются)
```python
def flatten(matrix):
    flattened_array = []
    for row in matrix:
        if isinstance(row, str):
            raise TypeError('Строка не имеет строк матрицы')
        for major in row:
            flattened_array.append(major)
    return flattened_array

print(flatten([[1,2],[3,4]]))
print(flatten([[1,2],(3,4,5)]))
print(flatten([[1],[],[2,3]]))
print(flatten([[1,2],'ab']))
```
![](./images/lab02/arrays.flatten.png)

## Задание B
### Функция №1 - транспонирование матрицы с проверкой на 'рваность' матрицы
```python
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
```
![](./images/lab02/matrix.transpose.png)

### Функция №2 - суммирование по строкам матрицы (с проверкой на 'рваность' матрицы)
```python
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
```
![](./images/lab02/matrix.row_sums.png)

### Функция №3 - суммирование по столбцам матрицы (с проверкой на 'рваность' матрицы)
```python
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
```
![](./images/lab02/matrix.col_sums.png)

## Задание C
### Получаем на вход кортеж и выдаем строку по определенному формату
```python
def format_record(record):
    if len(record) == 3: FIO, group,  gpa = record
    else: raise TypeError('Проверьте, что вы не забыли ввести все необходимое')
    if len(FIO.strip()) == 0: raise ValueError('ФИО должно содержать как минимум фамилию и имя')
    if len(group.strip()) == 0: raise ValueError('Группа не может быть пустой')
    if len(str(gpa).strip()) == 0: raise ValueError('GPA не может быть пустым')
    if not isinstance(gpa,float): raise ValueError('GPA необходимо вводить в формате float')
    if not 0.0 <= gpa <= 5.5: raise ValueError('GPA должен быть в диапазоне [0.0, 5.5]')

    FIO = FIO.split()
    group = group.strip()
    if 3 < len(FIO) < 2: raise TypeError('Необходимо ввести полное ФИО или имя и фаиилию')
    if len(FIO) == 2:
        new_FIO = FIO[0][0].upper() + FIO[0][1:].lower() + ' ' + FIO[1][0].upper() + '.'
    if len(FIO) == 3:
        new_FIO = FIO[0][0].upper() + FIO[0][1:].lower() + ' ' + FIO[1][0].upper() + '.' + FIO[2][0].upper() + '.'
    return f'{new_FIO}, гр. {group}, GPA {gpa:.2f}'

print(format_record(('Иванов Иван Иванович','BIVT-25',4.6)))
print(format_record(('Петров Пётр','IKBO-12',5.0)))
print(format_record(('Петров Пётр Петрович','IKBO-12',5.0)))
print(format_record(('  сидорова  анна   сергеевна ', 'ABB-01', 3.999)))
```
![](./images/lab02/tuples.png)