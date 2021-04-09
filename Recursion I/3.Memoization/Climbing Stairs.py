class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n < 3:
            return first if n == 1 else second
        else:
            third = 0
            for i in range(2, n):
                third = first + second
                first = second
                second = third
            return third


print(Solution.climbStairs(Solution, 4))
