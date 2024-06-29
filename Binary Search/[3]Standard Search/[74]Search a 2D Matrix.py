# You are given an m x n integer matrix matrix with the following two 
# properties: 
# 
#  
#  Each row is sorted in non-decreasing order. 
#  The first integer of each row is greater than the last integer of the 
# previous row. 
#  
# 
#  Given an integer target, return true if target is in matrix or false 
# otherwise. 
# 
#  You must write a solution in O(log(m * n)) time complexity. 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -10⁴ <= matrix[i][j], target <= 10⁴ 
#  
# 
#  Related Topics Array Binary Search Matrix 👍 15672 👎 416

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        # while top <= bottom:
        #     column_mid = top + (bottom - top) // 2  # 列中点
        #     if matrix[column_mid][0] > target:  # if 1st item in this row  is greater than target, target in bottom part
        #         bottom = column_mid - 1
        #     elif matrix[column_mid][-1] < target:  # if last item in the row is less than target, target in top part
        #         top = column_mid + 1
        #     else:  # matrix[mid][right] > target or matrix[mid][left] < target
        #         while left <= right:
        #             row_mid = left + (right - left) // 2
        #             if matrix[column_mid][row_mid] == target:
        #                 return True
        #             elif matrix[column_mid][row_mid] < target:
        #                 left = row_mid + 1
        #             else:
        #                 right = row_mid - 1
        #         break
        # return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // n][mid % n]  # mid // n is row, mid % n is column
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True)
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False)
print(Solution().searchMatrix(
    [[-8, -7, -5, -3, -3, -1, 1], [2, 2, 2, 3, 3, 5, 7], [8, 9, 11, 11, 13, 15, 17], [18, 18, 18, 20, 20, 20, 21],
     [23, 24, 26, 26, 26, 27, 27], [28, 29, 29, 30, 32, 32, 34]], -5) == True)
