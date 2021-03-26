class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # else:
        #     return self.myPow(x, n - 1) * x if n > 0 else 1 / (self.myPow(1 / x, n + 1) * x)

        res = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1 == 1:
                res *= x
            abs_n >>= 1
            x *= x
        return (1 / res) if n < 0 else res


if __name__ == "__main__":
    s = Solution()
    x = 2
    n = 2
    print(s.myPow(x, n))
