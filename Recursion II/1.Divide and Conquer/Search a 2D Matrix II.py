from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = 0
        column = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and column >= 0:
            if target == matrix[row][column]:
                return True
            elif target < matrix[row][column]:
                column -= 1
            elif target > matrix[row][column]:
                row += 1

        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = -1

# matrix = [[1, 2, 3], [4, 6, 7], [5, 8, 9]]
# target = 6

matrix = [[1, 1]]
target = 2
#
# matrix = [[2, 5], [2, 8], [7, 9], [7, 11], [9, 11]]
# target = 7

s = Solution()
print(s.searchMatrix(matrix, target))
