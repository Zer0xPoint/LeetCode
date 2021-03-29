class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n < 2:
            return first if n == 0 else second
        else:
            for i in range(1, n):
                third = first + second
                first = second
                second = third
            return third


print(Solution.fib(Solution, 4))
