class Solution:
    def climbStairs(self, n: int) -> int:
        fibs = [1, 2]
        for i in range(2, n):
            fibs.append(fibs[i - 1] + fibs[i - 2])
        return fibs[n - 1]


s = Solution()
print(s.climbStairs(4))
