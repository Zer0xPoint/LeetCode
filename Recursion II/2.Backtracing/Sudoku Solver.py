from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

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
                        return

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
