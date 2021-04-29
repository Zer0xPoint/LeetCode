from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def sub_grid_is_valid(row, column):
            nums_dict = defaultdict(int)
            for row_i in range(row, row + 3):
                for col_i in range(column, column + 3):
                    num = board[row_i][col_i]
                    if num != ".":
                        nums_dict[str(num)] += 1
                        if nums_dict[str(num)] > 1:
                            return False
            return True

        def row_is_valid(row_i):
            nums_dict = defaultdict(int)
            for col_i in range(9):
                num = board[row_i][col_i]
                if num != ".":
                    nums_dict[str(num)] += 1
                    if nums_dict[str(num)] > 1:
                        return False
            return True

        def col_is_valid(col_i):
            nums_dict = defaultdict(int)
            for row_i in range(9):
                num = board[row_i][col_i]
                if num != ".":
                    nums_dict[str(num)] += 1
                    if nums_dict[str(num)] > 1:
                        return False
            return True

        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                if not sub_grid_is_valid(row, column):
                    return False
        for row in range(0, 9):
            if not row_is_valid(row):
                return False

        for col in range(0, 9):
            if not col_is_valid(col):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    sudoku = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "1", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", "3", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(s.isValidSudoku(sudoku))
