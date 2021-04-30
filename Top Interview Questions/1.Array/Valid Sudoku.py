from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        sub_grid_set = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num != ".":
                    if num in row_set[row]:
                        return False
                    else:
                        row_set[row].add(num)

                    if num in col_set[col]:
                        return False
                    else:
                        col_set[col].add(num)

                    sub_grid_id = (row // 3) + (col // 3) * 3
                    if num in sub_grid_set[sub_grid_id]:
                        return False
                    else:
                        sub_grid_set[sub_grid_id].add(num)
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
