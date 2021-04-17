from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_in_row(row, num):
            for col in range(9):
                if board[row][col] == num:
                    return True
            return False

        def is_in_col(col, num):
            for row in range(9):
                if board[row][col] == num:
                    return True
            return False

        def is_in_subgrid(row, col, num):
            n_th_subgrid_row = row // 3
            n_th_subgrid_col = col // 3
            subgrid_start_row = n_th_subgrid_row * 3
            subgrid_start_col = n_th_subgrid_col * 3
            for i in range(subgrid_start_row, subgrid_start_row + 3):
                for j in range(subgrid_start_col, subgrid_start_col + 3):
                    print(i,j)
                    if board[i][j] == num:
                        return True
            return False

        def is_valid(row, col, num):
            if is_in_row(row, num):
                return False
            if is_in_col(col, num):
                return False
            if is_in_subgrid(row, col, num):
                return False
            return True

        def place_num(row, col, num):
            board[row][col] = num

        def remove_num(row, col):
            board[row][col] = "."

        def next_available_pos(row, col):
            for i in range(row, 9):
                for j in range(0, 9):
                    if i == 8 and j == 8:
                        return None, None
                    if board[i][j] == ".":
                        return i, j

        def helper(row=0, col=0):
            for num in range(1, 10):
                if is_valid(row, col, num):
                    place_num(row, col, num)
                    row, col = next_available_pos(row, col)
                    if row is None and col is None:
                        return
                    else:
                        helper(row, col)
                    remove_num(row, col)

        row, col = next_available_pos(0, 0)
        helper(row, col)


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
# print(board[0][1])
