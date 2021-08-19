import sys
from collections import Counter
from typing import List

nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

d = dict()
d[1] = 1
print(d)

for i in range(10, 5, -1):
    print(i)

print(0 // 3)
nums[0], nums[1], nums[2], nums[3] = nums[3], nums[2], nums[1], nums[0]
print(nums)

n = 321312
while n > 0:
    print(n % 10)
    n //= 10

print(-sys.maxsize)

print(Counter("aasdgawef"))

print("123".join("asdasd"))
t = ["123", "223", "323"]
# print(t[:][0])
print(list(zip(t)))

print("smiles"[1:5])
print("smiles".find("sm"))

nums = [1, 7, 3, 6, 5, 6]


def pivotIndex(nums: List[int]) -> int:
    l_idx = 1
    r_idx = len(nums) - 2
    l_sum, r_sum = nums[0], nums[-1]
    while l_idx <= r_idx:
        if l_sum == r_sum:
            return l_idx
        elif l_sum < r_sum:
            l_sum += nums[l_idx]
            l_idx += 1
        else:
            r_sum += nums[r_idx]
            r_idx -= 1
    return -1


print(pivotIndex(nums))


def searchInsert(nums: List[int], target: int) -> int:
    def binary_search(items, start, end, target):
        if end >= 1:
            mid_idx = start + (end - 1) // 2
            if items[mid_idx] == target:
                return mid_idx
            elif items[mid_idx] > target:
                return binary_search(items, start, mid_idx - 1, target)
            else:
                return binary_search(items, mid_idx + 1, end, target)
        else:
            return -1

    return binary_search(nums, 0, len(nums) - 1, target)


print("searchInsert")
print(searchInsert([1, 2, 4, 5], 0))


def merge(intervals: List[List[int]]) -> List[List[int]]:
    interval_length = len(intervals)
    intervals.sort(key=lambda x: x[0])
    if interval_length < 2:
        return intervals
    merges = list()
    for interval in intervals:
        if not merges or merges[-1][-1] < interval[0]:
            merges.append(interval)
        else:
            merges[-1][-1] = max(merges[-1][-1], interval[-1])
    return merges


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [0, 4]]
intervals = [[1, 4], [2, 3]]
print(merge(intervals))


