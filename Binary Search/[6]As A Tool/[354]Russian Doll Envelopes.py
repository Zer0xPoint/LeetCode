# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] 
# represents the width and the height of an envelope. 
# 
#  One envelope can fit into another if and only if both the width and height 
# of one envelope are greater than the other envelope's width and height. 
# 
#  Return the maximum number of envelopes you can Russian doll (i.e., put one 
# inside the other). 
# 
#  Note: You cannot rotate an envelope. 
# 
#  
#  Example 1: 
# 
#  
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] 
# => [5,4] => [6,7]).
#  
# 
#  Example 2: 
# 
#  
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= envelopes.length <= 10⁵ 
#  envelopes[i].length == 2 
#  1 <= wi, hi <= 10⁵ 
#  
# 
#  Related Topics Array Binary Search Dynamic Programming Sorting 👍 5963 👎 146
# 

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for w, h in envelopes:
            left, right = 0, len(dp)
            while left < right:
                mid = left + (right - left) // 2
                if dp[mid] < h:
                    left = mid + 1
                else:
                    right = mid
            if right == len(dp):
                dp.append(h)
            else:
                dp[right] = h
        return len(dp)


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))  # 3
print(Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]]))  # 1
