from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


if __name__ == '__main__':
    s = Solution()
    strings = ["h", "e", "l", "l", "o"]
    s.reverseString(strings)
    print(strings)
