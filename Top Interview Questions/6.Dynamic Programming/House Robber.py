from typing import List

'''
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''


class Solution:
    # memo = []

    def rob(self, nums: List[int]) -> int:
        # return self.rob_rec(len(nums) - 1, nums)
        # self.memo = [-1] * (len(nums))
        # return self.rob_rec_memo(len(nums) - 1, nums)
        # return self.rob_dp_memo(nums)
        return self.rob_dp_two_param(nums)

    def rob_rec(self, i, nums):
        if i < 0:
            return 0
        return max(self.rob_rec(i - 2, nums) + nums[i], self.rob_rec(i - 1, nums))

    def rob_rec_memo(self, i, nums):
        if i < 0:
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        self.memo[i] = max(self.rob_rec(i - 2, nums) + nums[i], self.rob_rec(i - 1, nums))
        return self.memo[i]

    def rob_dp_memo(self, nums):
        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i], dp[i - 1] + nums[i]))
            print(dp)
        return dp

    def rob_dp_two_param(self, nums):
        dp = [0, nums[0]]
        res = 0
        for i in range(1, len(nums)):
            res = max(dp[0], dp[1] + nums[i])
            if dp[0] > dp[1] + nums[i]:
                dp[1] = dp[1] + nums[i]
            dp[0] = dp[1]
            print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 9, 3, 1]
    # nums = [1, 2, 3, 1]
    # nums = [1, 2, 3]
    # nums = [1, 3, 1]
    # nums = [1, 1]
    # nums = [2, 1, 1, 2]
    print(s.rob(nums))
