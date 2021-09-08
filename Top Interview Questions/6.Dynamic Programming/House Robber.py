from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        pass
        i = 0
        dp = []
        while i < len(nums):
            if nums[i] > nums[i + 1]:
                dp.append(nums[i])
                i += 1
            else:
                dp.append(nums[i + 1])
                i += 2
            i += 1
        return dp


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 9, 3, 1]
    print(s.rob(nums))
