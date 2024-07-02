# Given a positive integer num, return true if num is a perfect square or false 
# otherwise. 
# 
#  A perfect square is an integer that is the square of an integer. In other 
# words, it is the product of some integer with itself. 
# 
#  You must not use any built-in library function, such as sqrt. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an 
# integer.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 2³¹ - 1 
#  
# 
#  Related Topics Math Binary Search 👍 4217 👎 305


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # low, high = 0, int(num)
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if mid ** 2 == num:
        #         return True
        #     elif mid ** 2 < num:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return False

        # if num < 2:
        #     return True
        # x = num // 2
        # while x ** 2 > num:
        #     # x = x - f(x)/ f'(x)
        #     # Newton Raphson method
        #     # x = x - ((x ** 2 - num) // (2 * x))
        #     x = (x + num // x) // 2
        # return x ** 2 == num

        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().isPerfectSquare(16))
print(Solution().isPerfectSquare(14))
print(Solution().isPerfectSquare(1))
print(Solution().isPerfectSquare(4))
print(Solution().isPerfectSquare(9))
