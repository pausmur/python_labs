from src.lab7.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab7.search import linear_search, binary_search, two_sum_brute, two_sum_fast
import random

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

if __name__ == '__main__':
    random.seed(42)
    x = 0
    for fn in (bubble_sort,insertion_sort,selection_sort):
        x += check_sorting(fn)
    x += check_search()
    x += check_two_sum()
    print(f'Ok, {x} проверок')







