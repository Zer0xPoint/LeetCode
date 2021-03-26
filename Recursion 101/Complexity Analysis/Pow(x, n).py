class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            return self.myPow(x, n - 1) * x if n > 0 else 1 / self.myPow(x, n + 1) * x


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2, -1))
