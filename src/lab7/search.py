def linear_search(nums, x) -> int:
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

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
            right = mid - 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return(i,j)
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        else:
            seen[x] = seen.get(x,0) or i
    return None

