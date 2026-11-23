# Лабораторная №7
## Задание 1 - поиск
### Линейный поиск - возвращает индекс первого вхождения, иначе -1. Шагов O(n)
```python
def linear_search(nums, x) -> int:
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1
```
### Бинарный поиск - возвращает индекс любого вхождения, иначе -1. Работает только на отсортированном списке, так как иначе он не будет определен. Шагов O(log n)
```python
def binary_search(sorted_nums, x) -> int:
    left = 0
    right = len(sorted_nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            left = mid + 1
        else:
            left = mid - 1
    return -1
```
### Two_sum через перебор пар - ищет пару индексов через перебор пар, сумма которых будет равна необходимому числу. Шагов O(n**2)
```python
def two_sum_brute(nums, target) -> tuple[int, int] | None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return(i,j)
    return None
```
### Two_sum через словарь - аналогично перебору пар ищет индексы, но быстрее с помощью словаря, совершая 1 проход. Шагов O(n)
```python
def two_sum_fast(nums, target) -> tuple[int, int] | None:
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        else:
            seen[x] = seen.get(x,0) or i
    return None
```
## Задание 2 - сортировки
### Сортировка пузырьком - проходим по списку, меняя местами соседей, если левый больше правого. Шагов O(n**2)
```python
def bubble_sort(nums) -> list:
    nums = list(nums)
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums(j + 1):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
```
### Сортировка выбором - находим минимум оставшей части и ставим его на место. Шагов O(n**2)
```python
def insertion_sort(nums) -> list:
    nums = list(nums)
    for i in range(1, nums):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j - 1] = temp
    return nums
```
### Сортировка вставками - берем элемент и сдвигаем его влево, пока он не встанет на место. Шагов O(n**2)
```python
def selection_sort(nums) -> list:
    nums = list(nums)
    for i in range(0, len(nums) - 1):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < smallest:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums
```

## Задание 3 - проверки против эталона
### check_sorting - создает случайные списки длиной от 0 до 50, элементы в которых принадлежат диапозону от -100 до 100 + проверка, что исходный список не был изменен
```python
def check_sorting(fn, trials = 100):
    for _ in range(trials):
        x = random.randint(0,50)
        nums = [random.randint(-100,100) for _ in range(x)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f'{fn.__name__} ошиблась на {nums}: {result}'
        assert nums == original, f'{fn.__name__} изменила исходный список'
    print(f'Ок: {fn.__name__}, {trials} проверок')
    return trials
```
### check_search - создает случайные списки и ищет элементы первого вхождения (для linear_search) или любого (для binary_search), также для случайно выбранного элемента. Проверка для обычного поиска, поиска не существующего числа и проверка на границе
```python
def check_search(trials = 100):
    for _ in range((trials + 1) // 2):
        x = random.randint(1,50)
        nums = [random.randint(-100,100) for _ in range(x)]
        need = random.choice(nums)
        assert linear_search(nums, need) == nums.index(need), (f'liner_search: {need} in {nums}')
        nums.sort()
        assert nums[binary_search(nums, need)] == need, (f'binary_search: {need} in {nums}')

    for _ in range((trials // 2 + 1) // 2):
        x = random.randint(0,50)
        nums = [random.randint(-100,100) for _ in range(x)]
        need = random.choice((random.randint(-200, -100), random.randint(100, 200)))
        assert linear_search(nums, need) == -1, (f'liner_search: {need} in {nums}')
        nums.sort()
        assert binary_search(nums, need) == -1, (f'binary_search: {need} in {nums}')

    for _ in range(trials // 4):
        x = random.randint(1,50)
        nums = [random.randint(-100, 100) for _ in range(x)]
        need = nums[random.choice((0, -1))]
        assert linear_search(nums, need) == nums.index(need), (f'liner_search: {need} in {nums}')
        nums.sort()
        assert nums[binary_search(nums, need)] == need, (f'binary_search: {need} in {nums}')

    print(f'Ok: linear_search, binary_search, {trials} проверок')
    return trials
```
### check_two_sum - создает случайные списки и случайное число для поиска и ищет пары чисел, сумма которых подходит числу
```python
def check_two_sum(trials = 100):
    for _ in range((trials + 1) // 2):
        x = random.randint(2,50)
        nums = [random.randint(-100,100) for _ in range(x)]
        a,b = random.sample(nums,2)
        c,d = two_sum_fast(nums,a+b)
        assert nums[c] + nums[d] == a + b, (f'two_sum_fast: {a} + {b} = {a + b} in {nums}')
        c,d = two_sum_brute(nums,a+b)
        assert nums[c] + nums[d] == a + b, (f'two_sum_brute: {a} + {b} = {a + b} in {nums}')

    for _ in range(trials // 2):
        x = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(x)]
        a = random.randint(100,200)
        b = random.randint(100,200)
        assert two_sum_fast(nums, a+b) is None, (f'two_sum_fast: {a} + {b} = {a + b} in {nums}')
        assert two_sum_brute(nums, a + b) is None, (f'two_sum_brute: {a} + {b} = {a + b} in {nums}')
    print(f'Ok: two_sum_fast, two_sum_brute, {trials} проверок')
    return trials
```
### main - подсчитывает общее число проверок
```python
if __name__ == '__main__':
    random.seed(42)
    x = 0
    for fn in (bubble_sort,insertion_sort,selection_sort):
        x += check_sorting(fn)
    x += check_search()
    x += check_two_sum()
    print(f'Ok, {x} проверок')
```
### Для запуска через терминал:

```py -m src.lab7.check```

### Вывод в терминале:
<img width="426" height="136" alt="check" src="https://github.com/user-attachments/assets/eea517d2-ac5b-4a84-a721-ac3bf3a019c6" />

## Задание 4 - бенчмарк
### Функция для записи и чтения csv файлов (чтобы помимо вывода в терминале бенчмарк сохранился в файле)
```python
def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]

def make_samples():
    for n in (1000,10000,100000):
        result = []
        for _ in range(100):
            nums = [random.randint(-100,100) for _ in range(n)]
            result.append(nums)
        write_csv(result, f'data/lab07/numbers_{n}.csv')
```
### Бенчмарк для сортировок:
```python
def bench_sorts(n):
    data = read_numbers(f'data/lab07/numbers_{n}.csv')
    rows = []
    for fn in (sorted, bubble_sort, insertion_sort, selection_sort):
        if n < 100000: 
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(('sort', n, fn.__name__, f'{t:.6f}'))
        else:
            rows.append(('sort', 100000, fn.__name__, '> 60 s'))
    return rows
```
### Бенчмарк для поисков и two_sum:
```python
def bench_search():
    targets = []
    data = [random.randint(-100000,100000) for _ in range(100000)]
    sorted_data = sorted(data)
    targets = [random.choice(data) for _ in range(10000)]
    rows = []

    t = timeit.timeit(lambda: [data.index(t) for t in targets], number = 1)
    rows.append(('search', 10000, 'index', f'{t:.6f}'))

    lt = timeit.timeit(lambda: [linear_search(data,t) for t in targets], number = 1)
    rows.append(('search', 10000, 'linear_search', f'{lt:.6f}'))

    st = timeit.timeit(lambda: sorted(data), number = 1)
    rows.append(('search', 10000, 'sorted_b4_bs',f'{st:.6f}'))

    bt = timeit.timeit(lambda: [binary_search(sorted_data,t) for t in targets], number = 1)
    rows.append(('search', 10000, 'binary_search', f'{bt:.6f}'))

    for n in [1000,10000]:
        data_two_sum = [random.randint(-1000000,1000000) for _ in range(n)]
        a,b =random.sample(data_two_sum,2)
        target = a + b

        ttsb = timeit.timeit(lambda: two_sum_brute(data_two_sum,target), number = 1)
        rows.append(('search', n, 'two_sum_brute', f'{ttsb:.6f}'))

        ttsf = timeit.timeit(lambda: two_sum_fast(data_two_sum,target), number = 1)
        rows.append(('search', n, 'two_sum_fast', f'{ttsf:.6f}'))

    return rows
```
### Функция main для связки бенчмарков и вывода в терминал
```python
def main():
    header = ('task','n','func','sec')
    rows = []
    for i in [1000,10000]:
        rows.extend(bench_sorts(i))
    rows.extend(bench_search())
    write_csv(rows, 'data/lab07/bench.csv', header)
    print('Бенчмарк')
    print(f'{'task':<12} | {'n':<8} | {'func':<20} | {'sec':<12}')
    print('-' * 60)
    for t, n, f, s in rows:
        print(f'{t:<12} | {n:<8} | {f:<20} | {s:<12}')
    print('-' * 60)
    print('Бенчмарк можно посмотреть в data/lab07/bench.csv')
```
### Для запуска через терминал:

```py -m src.lab7.bench```

### Пример вывода в терминале:
<img width="559" height="467" alt="bench terminal" src="https://github.com/user-attachments/assets/dae1226d-3d68-498e-85bf-e42a381667c6" />

### Пример вывода в csv файле:
<img width="428" height="429" alt="bench_csv" src="https://github.com/user-attachments/assets/cbcffed4-afbb-402f-b772-3402678458c5" />

