from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        result = []
        stack = []

        def helper(length, i):
            if length == k:
                return result.append(stack[:])
            for index in range(i, n):
                stack.append(nums[index])
                helper(length + 1, index + 1)
                stack.pop()

        helper(0, 0)

        return result


if __name__ == "__main__":
    s = Solution()
    n = 4
    k = 2
    print(s.combine(n, k))
