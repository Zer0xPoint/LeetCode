from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = nums[0]
        max_sub = sub
        for i in range(1, len(nums)):
            # max_sub = max(max_sub, max_sub + nums[i]) == max_sub + nums[i] ? max_sub + nums[i] : nums[i];
            sub = sub + nums[i] if max(nums[i], sub + nums[i]) == sub + nums[i] else nums[i]
            max_sub = max(max_sub, sub)

        return max_sub


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [5, 4, -1, 7, 8]
    s = Solution()
    print(s.maxSubArray(nums))
