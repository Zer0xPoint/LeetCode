from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        sorted_nums = []
        left_nums = self.sortArray(nums[:mid])
        right_nums = self.sortArray(nums[mid:])

        while left_nums and right_nums:
            if left_nums[0] < right_nums[0]:
                sorted_nums.append(left_nums.pop(0))
            else:
                sorted_nums.append(right_nums.pop(0))
        if left_nums:
            sorted_nums += left_nums
        if right_nums:
            sorted_nums += right_nums

        return sorted_nums
