from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            temp_profit = prices[i] - prices[i - 1]
            if temp_profit > 0:
                profit += temp_profit
            prices[i - 1] -= prices[i]
        return profit


if __name__ == '__main__':
    s = Solution()
    nums = [7, 1, 5, 8, 3, 6, 4]
    print(s.maxProfit(nums))
    # print(nums)
