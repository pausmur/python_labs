import csv
import random
import timeit
from src.lib.io_helpers import write_csv
from src.lab7.search import *
from src.lab7.sorting import *

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

if __name__ == '__main__':
    main()

    
