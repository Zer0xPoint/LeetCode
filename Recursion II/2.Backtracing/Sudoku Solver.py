from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # def is_sudoku():
        #     if "." not in set([val for row in board for val in row]):
        #         return True
        #
        # def not_in_row(row, num):
        #     return False if num in row else True
        #
        # def not_in_col(col, num):
        #     return False if num in col else True
        #
        # def not_in_sub_grid(sub_grid, num):
        #     return False if num in sub_grid else True
        #
        # def place_num(row, i, num):
        #     board[row][i] = num
        #
        # def remove_num(row, i):
        #     board[row][i] = "."
        #
        # for row in range(9):
        #     for i, val in enumerate(board[row]):
        #         if val == ".":
        #             col = list(zip(*board))[i]
        #             sub_row = (row // 3) * 3
        #             sub_col = (i // 3) * 3
        #             sub_gird = [board[i][j] for i in range(sub_row, sub_row + 3) for j in
        #                         range(sub_col, sub_col + 3)]
        #             for num in range(1, 10):
        #                 num = str(num)
        #                 if not_in_col(col, num) and not_in_row(board[row], num) and not_in_sub_grid(sub_gird, num):
        #                     place_num(row, i, num)
        #                     if is_sudoku():
        #                         return
        #                     else:
        #                         self.solveSudoku(board)
        #                     remove_num(row, i)
        def sudoku(puzzle):
            # base case: return result if no 0 left
            if "." not in set([v for r in puzzle for v in r]):
                return puzzle
            # iterate over every 0 value in the sudoku
            for row in range(len(puzzle)):
                for i, val in enumerate(puzzle[row]):
                    if val == ".":
                        # grab the column in which we check
                        col = list(zip(*puzzle))[i]
                        sq_row = (row // 3) * 3
                        sq_col = (i // 3) * 3
                        # grab the square in which we check
                        square = [puzzle[i][j] for i in range(sq_row, 3 + sq_row) for j in range(sq_col, 3 + sq_col)]
                        # iterate over every possible input
                        for candidate in range(1, 10):
                            # validate input
                            candidate = str(candidate)
                            if row_ok(candidate, puzzle[row]) and col_ok(candidate, col) and square_ok(candidate,
                                                                                                       square):
                                # if validated fill as value and continue
                                puzzle[row][i] = candidate
                                # if reached the filled validated sudoku - return
                                if sudoku(puzzle):
                                    return sudoku(puzzle)
                                # otherwise backtrack
                                else:
                                    puzzle[row][i] = "."
                        # if iterated over all possible candidates and no continuation - must backtrack
                        return False

        def row_ok(entry, row):
            return not (entry in row)

        def col_ok(entry, col):
            return not (entry in col)

        def square_ok(entry, square):
            return not (entry in square)

        sudoku(board)

s = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(board)
print(board)
