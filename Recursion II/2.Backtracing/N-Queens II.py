class Solution:
    def totalNQueens(self, n: int) -> int:

        res = []

        def is_not_under_attack(row, col):
            for exist_row in range(len(res)):
                exist_col = res[exist_row]
                if exist_col == col or exist_row == row:
                    return False
                elif exist_row + exist_col == row + col:
                    return False
                elif exist_row - exist_col == row - col:
                    return False

            return True

        def place_queen(row, col):
            res.append(col)

        def remove_queen(row, col):
            res.pop()

        def backtrack_nqueen(row=0, solution_count=0):
            for col in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        solution_count += 1
                    else:
                        # we move on to the next row
                        solution_count = backtrack_nqueen(row + 1, solution_count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            return solution_count

        return backtrack_nqueen()


s = Solution()
n = 4
print(s.totalNQueens(n))
