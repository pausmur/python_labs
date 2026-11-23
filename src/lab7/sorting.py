def bubble_sort(nums) -> list:
    nums = list(nums)
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

def insertion_sort(nums) -> list:
    nums = list(nums)
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
    return nums

def selection_sort(nums) -> list:
    nums = list(nums)
    for i in range(0, len(nums) - 1):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums

