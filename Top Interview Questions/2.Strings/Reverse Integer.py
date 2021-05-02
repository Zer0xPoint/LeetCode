import sys


class Solution:
    def reverse(self, x: int) -> int:
        symbol = 1 if x > 0 else -1
        x *= symbol
        result = 0
        while x != 0:
            pop = x % 10
            x //= 10
            result = result * 10 + pop
        return result * symbol if result < pow(2, 32) else 0


if __name__ == '__main__':
    s = Solution()
    num = -321
    print(s.reverse(num))
