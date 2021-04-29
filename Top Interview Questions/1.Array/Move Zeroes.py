from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        none_zer0_num = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[none_zer0_num] = nums[i]
                none_zer0_num += 1

        for i in range(none_zer0_num, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)
