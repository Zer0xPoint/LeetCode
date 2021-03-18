from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rec(s, head_index, tail_index):
            if s and head_index <= tail_index:
                s[head_index], s[tail_index] = s[tail_index], s[head_index],
                rec(s, head_index + 1, tail_index - 1)

        rec(s, 0, len(s) - 1)


solution = Solution()
s = ["H", "a", "n", "n", "a", "h"]
s = ["h", "e", "l", "l", "o"]
s = [1, 2, 3, 4, 5]
solution.reverseString(s)
print(s)
