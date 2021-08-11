def binary_search(items, start_idx, end_idx, target):
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if items[mid_idx] == target:
            return mid_idx
        elif items[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1

    return -1


nums = [1, 2, 3, 4, 6]
print(binary_search(nums, 0, len(nums) - 1, 5))
