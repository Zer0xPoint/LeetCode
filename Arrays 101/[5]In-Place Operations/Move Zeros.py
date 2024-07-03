from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_count_i = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                num_count_i += 1
                nums[num_count_i - 1] = nums[i]
                if num_count_i - 1 != i:
                    nums[i] = 0


if __name__ == "__main__":
    s = Solution()
    arr = [0, 1, 0, 3, 12]
    # arr = [3, 5, 5]
    arr = [1]
    # arr = [1, 0]
    print(s.moveZeroes(arr))
    print(arr)
