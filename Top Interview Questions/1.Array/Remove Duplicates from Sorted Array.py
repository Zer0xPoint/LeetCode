from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end, valid_num_count = 0, 0, 0
        while end < len(nums):
            if nums[end] > nums[start]:
                valid_num_count += 1
                nums[valid_num_count] = nums[end]
                start = end
            end += 1
        return valid_num_count + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9]
    nums = [1, 1, 2]
    s.removeDuplicates(nums)
    print(nums)
