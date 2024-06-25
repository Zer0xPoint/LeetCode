# Given a m x n matrix grid which is sorted in non-increasing order both row-
# wise and column-wise, return the number of negative numbers in grid. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[3,2],[1,0]]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 100 
#  -100 <= grid[i][j] <= 100 
#  
# 
#  
# Follow up: Could you find an 
# O(n + m) solution?
# 
#  Related Topics Array Binary Search Matrix 👍 4938 👎 132

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            count += len(row) - left
        return count


# leetcode submit region end(Prohibit modification and deletion)
# test from here

print(Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8)
print(Solution().countNegatives([[3, 2], [1, -1]]) == 1)
print(Solution().countNegatives([[-1]]) == 1)
print(Solution().countNegatives([[1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]), 0)
