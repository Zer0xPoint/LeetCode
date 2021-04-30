from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def reflect(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        transpose(matrix)
        reflect(matrix)


if __name__ == '__main__':
    s = Solution()
    nums = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(nums)
    print(nums)
