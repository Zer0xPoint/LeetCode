class Solution:
    def fib(self, n: int) -> int:
        nums = [0, 1]
        if n < 2:
            return nums[n]
        for i in range(1, n):
            nums.append(nums[i - 1] + nums[i])
        return nums[-1]


print(Solution.fib(Solution, 4))
