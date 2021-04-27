from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_i = 0
        pre_temp_num = nums[0]
        nums_len = len(nums)
        for i in range(nums_len + 1):
            temp_num = nums[temp_i]
            nums[temp_i] = pre_temp_num
            pre_temp_num = temp_num
            temp_i = (temp_i + k) % nums_len


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    # nums = [1, 2, 3, 4]
    k = 2
    s.rotate(nums, k)
    print(nums)
