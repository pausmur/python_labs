#Функция для возвращение минимума и максимума
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
print(min_max([1.5,2,2.0,-3.1]))
print(min_max([]))

#Функция для возвращения отсортированного списка уникальных значений
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

#Функция для расплющивания списка списков (матриц)
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
