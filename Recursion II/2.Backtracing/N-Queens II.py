class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col):
            pass

        def backtrack(param, count):
            pass

        def place_queen(row, col):
            pass

        def remove_queen(row, col):
            pass

        def backtrack_nqueen(row=0, count=0):
            for col in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            return count

        backtrack_nqueen()
