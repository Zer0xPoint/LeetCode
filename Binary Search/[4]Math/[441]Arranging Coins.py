# You have n coins and you want to build a staircase with these coins. The 
# staircase consists of k rows where the iᵗʰ row has exactly i coins. The last row of 
# the staircase may be incomplete. 
# 
#  Given the integer n, return the number of complete rows of the staircase you 
# will build. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 5
# Output: 2
# Explanation: Because the 3ʳᵈ row is incomplete, we return 2.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 8
# Output: 3
# Explanation: Because the 4ᵗʰ row is incomplete, we return 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  Related Topics Math Binary Search 👍 3853 👎 1323


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            total = (1 + mid) * mid // 2
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        return right


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().arrangeCoins(5) == 2)
print(Solution().arrangeCoins(8) == 3)
print(Solution().arrangeCoins(1) == 1)
print(Solution().arrangeCoins(0) == 0)
print(Solution().arrangeCoins(3) == 2)
print(Solution().arrangeCoins(1804289383) == 60070)
